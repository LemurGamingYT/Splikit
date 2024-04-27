from platform import system
from subprocess import run
from typing import Union
from pathlib import Path
from shutil import which

from antlr4 import FileStream, CommonTokenStream

from compiler.info import (
    get_info, op_name_to_symbol_map, DEFAULT_HEADER, is_function, is_type, is_method, is_property,
    is_static
)
from compiler.constants import (
    Code, EnvItem, Position, BOLD, RESET, RED, find_function, base_type, init_env
)
from compiler.basic_error_checker import BasicErrorChecker
from compiler.parser.SplikitVisitor import SplikitVisitor
from compiler.error_listener import SplikitErrorListener
from compiler.parser.SplikitParser import SplikitParser
from compiler.std import std_func, verify_params, LIBS
from compiler.parser.SplikitLexer import SplikitLexer


class SplikitCompiler(SplikitVisitor):
    def __init__(self, parent_env: Union[dict, None] = None) -> None:
        self.src: Union[str, None] = None
        self.env = parent_env or {}
        self.includes = set()

        self.info = get_info()

    def compile(self, file: Path) -> Path:
        self.src = file.read_text('utf-8')
        fstream = FileStream(file.as_posix())

        lexer = SplikitLexer(fstream)
        tokens = CommonTokenStream(lexer)

        parser = SplikitParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(SplikitErrorListener(self.src))

        tree = parser.parse()
        
        init_env(self.env, self.info)

        BasicErrorChecker(self.env.copy(), self.src).visit(tree)
        cpp_code = self.visit(tree)
        
        cpp_file = file.with_suffix('.cpp').absolute()
        includes = f'#include "{DEFAULT_HEADER.absolute().as_posix()}"\n'
        includes += ''.join(f'#include "{inc.absolute().as_posix()}"\n' for inc in self.includes)
        cpp_file.write_text(f'{includes}\n\n{cpp_code}', 'utf-8')
        return cpp_file

    def cpp_to_exe(self, spk_file: Path, cpp_file: Path, *args) -> Path:
        output: Path = spk_file.with_suffix('.exe' if system() == 'Windows' else '').absolute()
        if which('g++') is not None:
            run(['g++', cpp_file.as_posix(), '-o', output.as_posix(), *args])
        elif which('clang++') is not None:
            run(['clang++', cpp_file.as_posix(), '-o', output.as_posix(), *args])
        else:
            print(f'{BOLD}{RED}Invalid compiler{RESET}')
        
        return output

    def condition(self, ctx: SplikitParser.ExprContext) -> Code:
        expr = self.visit(ctx)
        if expr.type != 'bool':
            expr.text = f'to_bool({expr.text})'
            expr.type = 'bool'

        return expr

    def body_to_str(self, ctx: SplikitParser.BodyContext) -> str:
        return '\n'.join(map(lambda x: x.text + ';', self.visit(ctx)))
    
    def get_text(self, iterable: list) -> str:
        return ', '.join(map(lambda x: x.text, iterable))


    def visitParse(self, ctx: SplikitParser.ParseContext) -> str:
        return '\n'.join(map(lambda x: x.text, [self.visit(stmt) for stmt in ctx.stmt()]))

    def visitType(self, ctx: SplikitParser.TypeContext) -> str:
        if ctx.LBRACK() is not None:
            return f'array<{ctx.ID(1).getText()}>'

        return ctx.getText()

    def visitArg(self, ctx: SplikitParser.ArgContext) -> Code:
        return self.visit(ctx.expr())

    def visitArgs(self, ctx: SplikitParser.ArgsContext) -> list[Code]:
        return [self.visit(arg) for arg in ctx.arg()]

    def visitParam(self, ctx: SplikitParser.ParamContext) -> Code:
        typ = self.visitType(ctx.type_())
        return Code(
            f'{typ} {ctx.ID().getText()}',
            typ,
            Position(ctx.start.line, ctx.start.column)
        )

    def visitParams(self, ctx: SplikitParser.ParamsContext) -> list[Code]:
        return [self.visitParam(param) for param in ctx.param()]

    def visitBodyStmts(self, ctx: SplikitParser.BodyStmtsContext) -> Code:
        if ctx.RETURN():
            expr = self.visit(ctx.expr())
            return Code(f'return {expr.text}', expr.type, Position(ctx.start.line, ctx.start.column))
        elif ctx.stmt():
            return self.visit(ctx.stmt())

    def visitBody(self, ctx: SplikitParser.BodyContext) -> list[Code]:
        return [self.visit(body) for body in ctx.bodyStmts()]

    def visitIfStmt(self, ctx: SplikitParser.IfStmtContext) -> Code:
        condition = self.condition(ctx.expr())

        temp_env = self.env.copy()
        body = self.body_to_str(ctx.body())
        self.env = temp_env

        code = f'if ({condition.text}) {{\n{body}\n}}'
        if ctx.elseifStmt():
            for elseif in ctx.elseifStmt():
                code += self.visit(elseif).text

        if ctx.elseStmt():
            code += self.visit(ctx.elseStmt()).text

        return Code(
            code,
            condition.type,
            Position(ctx.start.line, ctx.start.column)
        )

    def visitElseifStmt(self, ctx: SplikitParser.ElseifStmtContext) -> Code:
        condition = self.condition(ctx.expr())

        temp_env = self.env.copy()
        body = self.body_to_str(ctx.body())
        self.env = temp_env

        return Code(
            f' else if ({condition.text}) {{\n{body}\n}}',
            condition.type,
            Position(ctx.start.line, ctx.start.column)
        )

    def visitElseStmt(self, ctx: SplikitParser.ElseStmtContext) -> Code:
        temp_env = self.env.copy()
        body = self.body_to_str(ctx.body())
        self.env = temp_env
        return Code(
            f' else {{\n{body}\n}}',
            'nil',
            Position(ctx.start.line, ctx.start.column)
        )

    def visitWhileStmt(self, ctx: SplikitParser.WhileStmtContext) -> Code:
        condition = self.condition(ctx.expr())

        temp_env = self.env.copy()
        body = self.body_to_str(ctx.body())
        self.env = temp_env

        return Code(
            f'while ({condition.text}) {{\n{body}\n}}',
            condition.type,
            Position(ctx.start.line, ctx.start.column)
        )
    
    def visitUseStmt(self, ctx: SplikitParser.UseStmtContext) -> Code:
        paths = [path.getText()[1:-1] for path in ctx.STRING()]
        position = Position(ctx.start.line, ctx.start.column)
        for path in paths:
            if path in LIBS:
                header = LIBS[path]
                self.includes.add(header)
                lib_info = get_info(header)
                
                new_info = {}
                for k, v in lib_info.items():
                    if is_type(k, v) or is_function(v):
                        continue

                    new_info[k] = v

                for _, v in lib_info.items():
                    if 'function' in v[0].split():
                        self.env[v[2]] = EnvItem(v[2], v[1], False)

                init_env(self.env, new_info)
                self.info |= new_info
            else:
                position.error_here(f'Unknown library \'{path}\'', self.src)

        return Code('', 'nil', position)

    def visitVarAssign(self, ctx: SplikitParser.VarAssignContext) -> Code:
        name = ctx.ID().getText()
        position = Position(ctx.start.line, ctx.start.column)
        if ctx.INCREMENT() is not None or ctx.DECREMENT() is not None:
            op = '++'
            if ctx.DECREMENT() is not None:
                op = '--'
            
            return Code(name + op, 'int', position)
        
        expr = self.visit(ctx.expr())
        typ = self.visit(ctx.type_()) if ctx.type_() else expr.type
        if (ctx.ADD() or ctx.SUB() or ctx.MUL() or ctx.DIV() or ctx.MOD()) is not None:
            op = ctx.ADD() and '+' or ctx.SUB() and '-' or ctx.MUL() and '*' or ctx.DIV() and '/' or\
                ctx.MOD() and '%'
            if op == '/' and expr.type == 'int' and self.env[name].type == 'int':
                return Code(f'{name} = div({name}, {expr.text}).quot', 'int', position)
            
            return Code(f'{name} = {self._op_symbol_to_name(op)}({name}, {expr.text})', typ, position)

        if name in self.env and ctx.CONST() is None and ctx.type_() is None:
            return Code(f'{name} = {expr.text}', typ, position)

        is_constant = ctx.CONST() is not None
        self.env[name] = EnvItem(name, typ, not is_constant)
        return Code(f'{"const " if is_constant else ""}{typ} {name} = {expr.text}', typ, position)

    def visitFuncAssign(self, ctx: SplikitParser.FuncAssignContext) -> Code:
        name = ctx.ID().getText()
        params = self.visit(ctx.params()) if ctx.params() else []
        typ = self.visit(ctx.type_()) if ctx.type_() else 'nil'

        param_dict = {}
        for param in params:
            splitted = param.text.split()
            param_dict[splitted[1]] = {'type': {splitted[0]}}

        @std_func(param_dict)
        def f(_, _env: dict, _call_position: Position) -> None:
            pass

        self.env[name] = EnvItem(name, typ, False, f)

        temp_env = self.env.copy()
        for param in params:
            splitted = param.text.split()
            self.env[splitted[1]] = EnvItem(splitted[1], splitted[0], False)

        body = self.body_to_str(ctx.body())

        self.env = temp_env
        inlined = 'inline ' if ctx.INLINE() else ''
        return Code(
            f"""{inlined}{typ} {name}({self.get_text(params)}) {{
{body}{"\nreturn nullptr;" if typ == 'nil' else ""}
}}
""",
            typ,
            Position(ctx.start.line, ctx.start.column)
        )

    def visitAtom(self, ctx: SplikitParser.AtomContext) -> Code:
        position = Position(ctx.start.line, ctx.start.column)
        if ctx.INT():
            return Code(ctx.getText(), 'int', position)
        elif ctx.FLOAT():
            return Code(ctx.getText() + 'f', 'float', position)
        elif ctx.STRING():
            return Code(ctx.getText(), 'string', position)
        elif ctx.BOOL():
            return Code(ctx.getText(), 'bool', position)
        elif ctx.NIL():
            return Code(ctx.getText(), 'nil', position)
        elif ctx.ID():
            return Code(ctx.getText(), self.env[ctx.ID().getText()].type, position)
        elif ctx.expr():
            expr = self.visit(ctx.expr())
            expr.text = f'({expr.text})'
            return expr
        elif ctx.LBRACE():
            typ = self.visit(ctx.type_())
            args = self.visit(ctx.args()) if ctx.args() else []
            return Code(
                f'new_array<{typ}>({{{self.get_text(args)}}})',
                f'array<{typ}>', position
            )

    def visitCall(self, ctx: SplikitParser.CallContext) -> Code:
        callee = self.env.get(ctx.ID().getText())
        position = Position(ctx.start.line, ctx.start.column)
        args = self.visit(ctx.args()) if ctx.args() else []
        if callee.callable is not None:
            out = callee.callable(self, args, position)
            if out is not None:
                return out

        return Code(
            f'{callee.name}({self.get_text(args)})',
            callee.type,
            position
        )

    def _op_symbol_to_name(self, op: str) -> str:
        return list(op_name_to_symbol_map.keys())[list(op_name_to_symbol_map.values()).index(op)]

    def visitExpr(self, ctx: SplikitParser.ExprContext) -> Code:
        if ctx.atom():
            return self.visit(ctx.atom())
        elif ctx.call():
            return self.visit(ctx.call())
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            left_type = base_type(left.type)
            right = self.visit(ctx.expr(1))
            right_type = base_type(right.type)
            op = ctx.op.text

            position = Position(ctx.op.line, ctx.op.column)
            
            # manually add int divided by int because C++ already has a div(int, int) and it cannot
            # be overriden
            if op == '/' and left_type == 'int' and right_type == 'int':
                return Code(f'div({left.text}, {right.text}).quot', 'int', position)
            elif left_type == 'any' and right_type == 'any':
                typ = left.type
            else:
                info_item = self.info.get((op, (left_type, right_type)))
                typ = info_item[1]

            name = self._op_symbol_to_name(op)
            return Code(f'{name}({left.text}, {right.text})', typ, position)
        elif ctx.NOT():
            left = self.visit(ctx.expr(0))
            left_type = base_type(left.type)
            info_item = self.info.get(('!', (left_type,)))
            position = Position(ctx.start.line, ctx.start.column)
            if info_item is None:
                return Code(
                    f'!to_bool({left.text})',
                    'bool',
                    position
                )

            return Code(f'not_({left.text})', info_item[1], position)
        elif ctx.DOT():
            left = self.visit(ctx.expr(0))
            ltype = left.type
            if ltype.startswith('array<'):
                ltype = 'array'

            attr = ctx.ID().getText()
            info_item = find_function(self.info, f'{ltype}_{attr}')
            position = Position(ctx.start.line, ctx.start.column)
            if info_item is None:
                position.error_here(f'\'{ltype}\' has no attribute \'{attr}\'', self.src)

            # if info_item[2].split(', ')[0].split()[0].startswith('array<') and ltype == 'array':

            args = []
            if not is_static(info_item):
                args.append(left)

            if is_property(info_item):
                return Code(
                    f'{ltype}_{attr}({self.get_text(args)})',
                    info_item[1],
                    position
                )
            elif is_method(info_item):
                args.extend(self.visit(ctx.args()) if ctx.args() else [])
                params_dict = {}
                for param in info_item[3].split(', '):
                    if param == '':
                        continue

                    splitted = param.split()
                    params_dict[splitted[1]] = {'type': {splitted[0]}}

                verify_params(args, params_dict, self, position)
                return Code(
                    f'{ltype}_{attr}({self.get_text(args)})',
                    info_item[1],
                    position
                )
            else:
                position.error_here(f'\'{attr}\' is an invalid attribute', self.src)
