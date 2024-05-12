from dataclasses import dataclass
from pprint import pprint
from pathlib import Path

from compiler.info import (
    get_info, is_method, is_property, is_function, is_type, has_overload
)
from compiler.constants import Position, base_type, find_function, EnvItem, init_env
from compiler.parser.SplikitVisitor import SplikitVisitor
from compiler.parser.SplikitParser import SplikitParser
from compiler.std import LIBS


@dataclass(slots=True, unsafe_hash=True, eq=False)
class CheckerNode:
    type: str

@dataclass(slots=True, unsafe_hash=True, eq=False)
class Param:
    name: str
    checker_node: CheckerNode


class BasicErrorChecker(SplikitVisitor):
    def __init__(self, parent_env: dict, src: str) -> None:
        self.info = get_info()
        self.env = parent_env
        self.src = src
    
    
    def apply_params(self, params: list[CheckerNode]) -> None:
        for param in params:
            self.env[param.name] = EnvItem(param.name, param.checker_node.type, False)
    

    def visitType(self, ctx: SplikitParser.TypeContext) -> str:
        if ctx.LBRACK() is not None:
            return f'array<{ctx.ID(1).getText()}>'

        return ctx.getText()
    
    def visitArgs(self, ctx: SplikitParser.ArgsContext) -> list[CheckerNode]:
        return [self.visit(arg) for arg in ctx.arg()]
    
    def visitParam(self, ctx: SplikitParser.ParamContext) -> Param:
        return Param(ctx.ID().getText(), CheckerNode(self.visit(ctx.type_())))
    
    def visitParams(self, ctx: SplikitParser.ParamsContext) -> list[Param]:
        return [self.visit(param) for param in ctx.param()]
    
    def add_info(self, instance, info: dict) -> None:
        new_info = {}
        for k, v in info.items():
            if is_type(v) or is_function(v):
                continue

            new_info[k] = v

        for _, v in info.items():
            if is_function(v):
                instance.env[v.name] = EnvItem(v.name, v.return_type, False)

        init_env(instance.env, new_info)
        instance.info |= new_info
    
    def visitUseStmt(self, ctx: SplikitParser.UseStmtContext) -> CheckerNode:
        paths = [path.getText()[1:-1] for path in ctx.STRING()]
        position = Position(ctx.start.line, ctx.start.column)
        for path in paths:
            if path in LIBS:
                header = LIBS[path]
                lib_info = get_info(header)
                self.add_info(self, lib_info)
            else:
                position.error_here(f'Unknown library \'{path}\'', self.src)

        return CheckerNode('nil')
    
    def visitVarAssign(self, ctx: SplikitParser.VarAssignContext) -> CheckerNode:
        name = ctx.ID().getText()
        position = Position(ctx.start.line, ctx.start.column)
        if ctx.INCREMENT() is not None or ctx.DECREMENT() is not None:
            if name not in self.env:
                position.error_here(f'Variable \'{name}\' is not defined', self.src)
            elif name in self.env and base_type(self.env[name].type) != 'int':
                position.error_here(f'Only integers can be incremented', self.src)
            
            return CheckerNode('int')
        else:
            expr = self.visit(ctx.expr())
            typ = self.visit(ctx.type_()) if ctx.type_() else expr.type
            if typ != expr.type:
                position.error_here(
                    f'Value (type \'{expr.type}\') does not match variable annotation \'{typ}\'',
                    self.src
                )
            
            if (ctx.ADD() or ctx.SUB() or ctx.MUL() or ctx.DIV() or ctx.MOD()) is not None:
                if name not in self.env:
                    position.error_here(f'Variable \'{name}\' is not defined', self.src)
                
            if name in self.env and ctx.CONST() is None and ctx.type_() is None:
                item = self.env[name]
                if not item.can_be_changed:
                    position.error_here(f'Variable \'{name}\' is constant', self.src)
                elif base_type(item.type) != base_type(typ):
                    position.error_here(
                        f'Variable type \'{item.type}\' does not match expression type \'{typ}\'',
                        self.src
                    )

            if name in self.env and ctx.CONST() is not None:
                position.error_here(
                    f'\'{name}\' cannot be defined as a constant when already defined',
                    self.src
                )
            elif name in self.env and ctx.type_() is not None:
                position.error_here(
                    f'\'{name}\' cannot be defined with a new type when already defined',
                    self.src
                )
        
            self.env[name] = EnvItem(name, typ, ctx.CONST() is None)
            return CheckerNode('nil')
    
    def visitFuncAssign(self, ctx: SplikitParser.FuncAssignContext) -> CheckerNode:
        name = ctx.ID().getText()
        if find_function(self.info, name) is not None:
            Position(ctx.ID().getSymbol().line, ctx.ID().getSymbol().column).error_here(
                f'Function \'{name}\' is reserved for the compiler', self.src
            )

        typ = self.visit(ctx.type_()) if ctx.type_() else 'nil'
        if name == 'main' and typ != 'int':
            Position(ctx.type_().start.line, ctx.type_().start.column).error_here(
                'main function must return an int', self.src
            )

        self.env[name] = EnvItem(name, typ, False)

        temp_env = self.env.copy()
        params = self.visit(ctx.params()) if ctx.params() else []
        self.apply_params(params)

        self.visit(ctx.body())

        self.env = temp_env
        return CheckerNode('nil')

    def visitAtom(self, ctx: SplikitParser.AtomContext) -> CheckerNode:
        if ctx.INT() is not None:
            return CheckerNode('int')
        elif ctx.FLOAT() is not None:
            return CheckerNode('float')
        elif ctx.STRING() is not None:
            return CheckerNode('string')
        elif ctx.BOOL() is not None:
            return CheckerNode('bool')
        elif ctx.NIL() is not None:
            return CheckerNode('nil')
        elif ctx.ID() is not None:
            if ctx.ID().getText() in self.env:
                return CheckerNode(self.env[ctx.ID().getText()].type)
            else:
                Position(ctx.start.line, ctx.start.column).error_here(
                    f'Undefined object \'{ctx.ID().getText()}\'', self.src
                )
        elif ctx.expr() is not None:
            return self.visit(ctx.expr())
        elif ctx.LBRACE() is not None:
            typ = self.visit(ctx.type_())
            args = self.visit(ctx.args()) if ctx.args() else []
            for arg in args:
                if arg.type != typ:
                    Position(ctx.start.line, ctx.start.column).error_here(
                        f'Value (type \'{arg.type}\') does not match variable annotation \'{typ}\'',
                        self.src
                    )

            return CheckerNode(f'array<{typ}>')
        elif ctx.REGEX() is not None:
            return CheckerNode('regex')
    
    def visitCall(self, ctx: SplikitParser.CallContext) -> CheckerNode:
        name = ctx.ID().getText()
        position = Position(ctx.start.line, ctx.start.column)
        if name not in self.env:
            position.error_here(f'Undefined object \'{name}\'', self.src)
        
        return CheckerNode(self.env[name].type)
    
    def visitExpr(self, ctx: SplikitParser.ExprContext) -> CheckerNode:
        if ctx.atom() is not None:
            return self.visit(ctx.atom())
        elif ctx.call() is not None:
            return self.visit(ctx.call())
        elif ctx.SUB() is not None:
            expr = self.visit(ctx.expr(0))
            position = Position(ctx.start.line, ctx.start.column)
            if expr.type not in {'int', 'float'}:
                position.error_here(f'Invalid type \'{expr.type}\' for unary \'-\'', self.src)
            
            return CheckerNode(expr.type)
        elif ctx.op is not None:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            position = Position(ctx.start.line, ctx.start.column)
            op = ctx.op.text
            
            if left.type == 'any' and right.type == 'any':
                position.info_here(f'any + any could end up in an error', self.src)
                typ = left.type
            else:
                info_item = find_function(self.info, op)
                if info_item is None:
                    position.error_here(
                        f'Invalid operation \'{op}\' on types \'{left.type}\' and \'{right.type}\'',
                        self.src
                    )
                
                typ = info_item.return_type
            
            return CheckerNode(typ)
        elif ctx.NOT() is not None:
            left = self.visit(ctx.expr(0))
            info_item = find_function(self.info, '!')
            position = Position(ctx.start.line, ctx.start.column)
            if info_item is None or not has_overload(info_item, [left.type]):
                position.info_here(
                    f'\'{left.type}\' has no operation \'not\', inverting to_bool({left.type})',
                    self.src
                )
                
                return CheckerNode('bool')

            return CheckerNode(info_item.return_type)
        elif ctx.DOT() is not None:
            left = self.visit(ctx.expr(0))
            ltype = left.type
            if ltype.startswith('array<'):
                ltype = 'array'

            attr = ctx.ID().getText()
            info_item = find_function(self.info, f'{ltype}_{attr}')
            position = Position(ctx.start.line, ctx.start.column)
            if info_item is None:
                position.error_here(f'\'{ltype}\' has no attribute \'{attr}\'', self.src)
            
            if is_property(info_item) or is_method(info_item):
                return CheckerNode(info_item.return_type)
            else:
                position.error_here(f'\'{attr}\' is an invalid attribute', self.src)
