from argparse import Namespace
from typing import Union
from pathlib import Path

from antlr4 import FileStream, CommonTokenStream

from compiler.info import get_info, op_name_to_symbol_map
from compiler.parser.SplikitVisitor import SplikitVisitor
from compiler.error_listener import SplikitErrorListener
from compiler.parser.SplikitParser import SplikitParser
from compiler.constants import Code, EnvItem, Position
from compiler.parser.SplikitLexer import SplikitLexer


class SplikitCompiler(SplikitVisitor):
    def __init__(self, args: Namespace, parent_env: Union[dict, None] = None) -> None:
        self.src: Union[str, None] = None
        self.env = parent_env or {}
        self.args = args

        self.info = get_info()
        self.env.update({
            k: EnvItem(k, k)
            for k, v in self.info.items()
            if k == v
        })

    
    def compile(self, file: Path) -> str:
        self.src = file.read_text('utf-8')
        fstream = FileStream(file.as_posix())
        
        lexer = SplikitLexer(fstream)
        tokens = CommonTokenStream(lexer)
        
        parser = SplikitParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(SplikitErrorListener(self.src))
        
        tree = parser.parse()
        return self.visit(tree)
    
    def find_function(self, name: str) -> Union[tuple, None]:
        for func in self.info.values():
            if isinstance(func, tuple) and func[2] == name:
                return func
    
    def condition(self, ctx: SplikitParser.ExprContext) -> Code:
        expr = self.visit(ctx)
        if expr.type != 'bool':
            expr.text = f'to_bool({expr.text})'
            expr.type = 'bool'
        
        return expr
    
    def body_to_str(self, ctx: SplikitParser.BodyContext) -> str:
        return '\n'.join(map(lambda x: x.text + ';', self.visit(ctx)))
    
    
    def visitParse(self, ctx: SplikitParser.ParseContext) -> str:
        return '\n'.join(map(lambda x: x.text, [self.visit(stmt) for stmt in ctx.stmt()]))
    
    def visitType(self, ctx: SplikitParser.TypeContext) -> str:
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
                code += f' {self.visit(elseif).text}'

        if ctx.elseStmt():
            code += f' else {{\n{self.visit(ctx.elseStmt()).text}\n}}'
        
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
            f'else if ({condition.text}) {{\n{body}\n}}',
            condition.type,
            Position(ctx.start.line, ctx.start.column)
        )
    
    def visitElseStmt(self, ctx: SplikitParser.ElseStmtContext) -> Code:
        temp_env = self.env.copy()
        body = self.body_to_str(ctx.body())
        self.env = temp_env
        return Code(
            body,
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
    
    def visitVarAssign(self, ctx: SplikitParser.VarAssignContext) -> Code:
        name = ctx.ID().getText()
        expr = self.visit(ctx.expr())
        typ = self.visit(ctx.type_()) if ctx.type_() else expr.type
        position = Position(ctx.start.line, ctx.start.column)
        if typ != expr.type:
            position.error_here(
                f'Variable (type \'{expr.type}\') does not match annotated type (\'{typ}\')',
                self.src
            )

        if name in self.env:
            return Code(f'{name} = {expr.text}', typ, position)

        self.env[name] = EnvItem(name, typ)
        return Code(f'{typ} {name} = {expr.text}', typ, position)
    
    def visitFuncAssign(self, ctx: SplikitParser.FuncAssignContext) -> Code:
        name = ctx.ID().getText()
        if self.find_function(name) is not None:
            Position(ctx.ID().getSymbol().line, ctx.ID().getSymbol().column).error_here(
                f'Function \'{name}\' is reserved for the compiler', self.src
            )
        
        params = self.visit(ctx.params()) if ctx.params() else []
        typ = self.visit(ctx.type_())
        if name == 'main' and typ != 'int':
            Position(ctx.type_().start.line, ctx.type_().start.column).error_here(
                'main function must return an int', self.src
            )

        self.env[name] = EnvItem(name, typ)

        temp_env = self.env.copy()
        for param in params:
            splitted = param.text.split()
            self.env[splitted[1]] = EnvItem(splitted[1], splitted[0])

        body = self.body_to_str(ctx.body())

        self.env = temp_env
        return Code(
            f"""{typ} {name}({", ".join(map(lambda x: x.text, params))}) {{
{body}
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
            item = self.env.get(ctx.ID().getText())
            if item is None:
                position.error_here(f'Undefined object {ctx.ID().getText()}', self.src)
            
            return Code(ctx.getText(), item.type, position)
        elif ctx.expr():
            expr = self.visit(ctx.expr())
            expr.text = f'({expr.text})'
            return expr
    
    def visitCall(self, ctx: SplikitParser.CallContext) -> Code:
        callee = self.env.get(ctx.ID().getText())
        position = Position(ctx.start.line, ctx.start.column)
        if callee is None:
            position.error_here(f'Undefined object {ctx.ID().getText()}', self.src)

        args = self.visit(ctx.args()) if ctx.args() else []
        if callee.callable is not None:
            return callee.callable(self, args, position, self.src)

        return Code(
            f'{callee.name}({", ".join(map(lambda x: x.text, args))})',
            callee.type,
            position
        )
    
    def visitExpr(self, ctx: SplikitParser.ExprContext) -> Code:
        if ctx.atom():
            return self.visit(ctx.atom())
        elif ctx.call():
            return self.visit(ctx.call())
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            position = Position(ctx.op.line, ctx.op.column)
            info_item = self.info.get((op, (left.type, right.type)))
            if info_item is None:
                position.error_here(
                    f'Invalid operation \'{op}\' on types \'{left.type}\' and \'{right.type}\'',
                    self.src
                )
            
            name = list(op_name_to_symbol_map.keys())[list(op_name_to_symbol_map.values()).index(op)]
            return Code(
                f'{name}({left.text}, {right.text})',
                info_item[1],
                position
            )
        elif ctx.NOT():
            left = self.visit(ctx.expr(0))
            info_item = self.info.get((left.type, ('not_',)))
            position = Position(ctx.start.line, ctx.start.column)
            if info_item is None:
                position.error_here(
                    f'Invalid operation \'not\' on type \'{left.type}\'',
                    self.src
                )

            return Code(
                f'not_({left.text})',
                info_item[1],
                position
            )
        elif ctx.DOT():
            left = self.visit(ctx.expr(0))
            attr = ctx.ID().getText()
            info_item = self.find_function(f'{left.type}_{attr}')
            position = Position(ctx.start.line, ctx.start.column)
            if info_item is None:
                position.error_here(f'\'{left.type}\' has no attribute \'{attr}\'', self.src)
            
            comments = info_item[0].split()
            args = []
            if 'static' not in comments:
                args.append(left)
            
            if 'property' in comments:
                return Code(
                    f'{left.type}_{attr}({", ".join(map(lambda x: x.text, args))})',
                    info_item[1],
                    position
                )
            elif 'method' in comments:
                args.extend(self.visit(ctx.args()) if ctx.args() else [])
                return Code(
                    f'{left.type}_{attr}({", ".join(map(lambda x: x.text, args))})',
                    info_item[1],
                    position
                )
            else:
                position.error_here(f'\'{attr}\' is an invalid attribute', self.src)
