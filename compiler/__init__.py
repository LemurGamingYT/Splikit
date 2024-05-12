from platform import system
from subprocess import run
from pprint import pprint
from typing import Union
from pathlib import Path
from shutil import which

from antlr4 import InputStream, CommonTokenStream

from compiler.info import (
    get_info, op_name_to_symbol_map, DEFAULT_HEADER, is_method, is_property,
    is_static, has_overload
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
    
    @property
    def error_checker(self) -> Union[BasicErrorChecker, None]:
        return self._error_checker if hasattr(self, '_error_checker') else None
    
    def compile_string(self, src: str, compiler: Union['SplikitCompiler', None] = None) -> str:
        sub_env = self.env.copy()
        init_env(sub_env, self.info)
        
        if compiler is None:
            compiler = SplikitCompiler(sub_env)

        istream = InputStream(src)

        lexer = SplikitLexer(istream)
        tokens = CommonTokenStream(lexer)

        parser = SplikitParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(SplikitErrorListener(self.src))

        tree = parser.parse()

        self._error_checker = BasicErrorChecker(sub_env.copy(), self.src)
        self._error_checker.info = compiler.info
        self._error_checker.visit(tree)
        # pprint(self._error_checker.info)

        return compiler.visit(tree)

    def compile(self, file: Path, extension: str = '.cpp') -> Path:
        self.src = file.read_text('utf-8')
        init_env(self.env, self.info)

        cpp_code = self.compile_string(self.src, self)
        
        cpp_file = file.with_suffix(extension).absolute()
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
    
    def get_text(self, iterable: list) -> str:
        return ', '.join(map(lambda x: x.text, iterable))
    
    def body_to_str(self, ctx: SplikitParser.BodyContext) -> str:
        return '\n'.join(map(lambda x: x.text + ';', self.visit(ctx)))
    
    def interpolate_string(self, s: str, position: Position) -> str:
        if s.startswith('$'):
            i = 0
            output_string = ''
            string_type = s[1]
            error_message = f'Use of {string_type} in outer string, can\'t use in inner string'
            s = s[2:-1]
            while i < len(s):
                if i + 1 > len(s):
                    continue
                
                char = s[i]
                
                if char == '{':
                    concatenation = ''
                    for c in s[i+1:-1]:
                        if c == '}':
                            break
                        elif c == string_type:
                            position.error_here(error_message, self.src)

                        concatenation += c

                        i += 1

                    code = self.compile_string(concatenation, self)
                    output_string += f'" + repr({code}) + "'
                    i += 1
                else:
                    output_string += char

                i += 1
            
            return f'"{output_string}"'
        
        return f'"{s[1:-1]}"'

    def get_body(self, ctx: SplikitParser.BodyContext, params: list[Code]) -> str:
        temp_env = self.env.copy()
        for param in params:
            splitted = param.text.split()
            self.env[splitted[1]] = EnvItem(splitted[1], splitted[0], False)
        
        body = self.body_to_str(ctx)
        
        self.env = temp_env
        return body


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

    def visitForeachStmt(self, ctx: SplikitParser.ForeachStmtContext) -> Code:
        var = ctx.ID().getText()
        expr = self.visit(ctx.expr())
        
        temp_env = self.env.copy()
        self.env[var] = EnvItem(var, expr.type, False)
        
        body = self.body_to_str(ctx.body())
        self.env = temp_env
        
        return Code(
            f'for (auto {var} : {expr.text}) {{\n{body}\n}}',
            'nil',
            Position(ctx.start.line, ctx.start.column)
        )

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
                if self.error_checker is not None:
                    self.error_checker.add_info(self, lib_info)
            else:
                position.error_here(f'Unknown library \'{path}\'', self.src)

        return Code(f'// {", ".join(paths)} used', 'nil', position)

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
        def f(*_) -> None:
            pass

        self.env[name] = EnvItem(name, typ, False, f)

        body = self.get_body(ctx.body(), params)
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
        if ctx.INT() is not None:
            return Code(ctx.getText(), 'int', position)
        elif ctx.FLOAT() is not None:
            return Code(ctx.getText() + 'f', 'float', position)
        elif ctx.STRING() is not None:
            return Code(self.interpolate_string(ctx.getText(), position), 'string', position)
        elif ctx.BOOL() is not None:
            return Code(ctx.getText(), 'bool', position)
        elif ctx.NIL() is not None:
            return Code(ctx.getText(), 'nil', position)
        elif ctx.ID() is not None:
            return Code(ctx.getText(), self.env[ctx.ID().getText()].type, position)
        elif ctx.expr() is not None:
            expr = self.visit(ctx.expr())
            expr.text = f'({expr.text})'
            return expr
        elif ctx.LBRACE() is not None:
            typ = self.visit(ctx.type_())
            args = self.visit(ctx.args()) if ctx.args() else []
            return Code(
                f'new_array<{typ}>({{{self.get_text(args)}}})',
                f'array<{typ}>', position
            )
        elif ctx.REGEX() is not None:
            return Code(
                f'new_regex("{ctx.getText()[1:-1].replace("\\", "\\\\")}")',
                'regex', position
            )
    
    def _inline_call(
        self, info_name: str, args: list[Code], func_name: Union[str, None] = None
    ) -> str:
        if func_name is None:
            func_name = info_name

        if info_name in self.info:
            f = self.info[info_name]
            code = ''
            for comment in f.comments:
                if comment.startswith('single-return('):
                    comment = comment[14:-1]
                    code = comment
                    for i, arg in enumerate(args, start=1):
                        code = code.replace(f'@{i}@', arg.text)

                    return code

        return f'{func_name}({self.get_text(args)})'

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
        if ctx.atom() is not None:
            return self.visit(ctx.atom())
        elif ctx.call() is not None:
            return self.visit(ctx.call())
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            left_type = base_type(left.type)
            right = self.visit(ctx.expr(1))
            right_type = base_type(right.type)
            op = ctx.op.text

            position = Position(ctx.op.line, ctx.op.column)
            
            # manually add int / int, C++ already has a div(int, int) and it cannot be overriden
            if op == '/' and left_type == 'int' and right_type == 'int':
                return Code(f'{left.text} / {right.text}', 'int', position)
            elif left_type == 'any' and right_type == 'any':
                typ = left.type
            else:
                info_item = find_function(self.info, op)
                typ = info_item.return_type

            name = self._op_symbol_to_name(op)
            return Code(self._inline_call(op, [left, right], name), typ, position)
        elif ctx.NOT():
            left = self.visit(ctx.expr(0))
            left_type = base_type(left.type)
            info_item = find_function(self.info, '!')
            position = Position(ctx.start.line, ctx.start.column)
            if info_item is None or not has_overload(info_item, [left_type]):
                call = self._inline_call('to_bool', [left])
                return Code(
                    f'!{call}',
                    'bool',
                    position
                )

            return Code(self._inline_call('!', [left], 'not_'), info_item.return_type, position)
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

            args = []
            if not is_static(info_item):
                args.append(left)

            if is_property(info_item):
                call = self._inline_call(f'{ltype}_{attr}', args)
                return Code(
                    call,
                    info_item.return_type,
                    position
                )
            elif is_method(info_item):
                args.extend(self.visit(ctx.args()) if ctx.args() else [])
                params_dict = {}
                for name, typ in zip(info_item.overloads[0][1], info_item.overloads[0][0]):
                    params_dict[name] = {'type': {typ}}

                verify_params(args, params_dict, self, position)
                call = self._inline_call(f'{ltype}_{attr}', args)
                return Code(
                    call,
                    info_item.return_type,
                    position
                )
        elif ctx.SUB() is not None:
            expr = self.visit(ctx.expr(0))
            return Code(ctx.getText(), expr.type, Position(ctx.start.line, ctx.start.column))
