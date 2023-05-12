from .gen.SplikitVisitor import SplikitVisitor
from .gen.SplikitParser import SplikitParser
from .env import Environment
from .error import report_error
from .other.funcs import Funcs
from .other.libs import Libs
from .objects import *


class Visitor(SplikitVisitor):
    def __init__(self, environment: Environment) -> None:
        self.env = environment

    def visitVariableDeclaration(self, ctx:SplikitParser.VariableDeclarationContext):
        name = ctx.Identifier().getText()
        value = self.visit(ctx.expression())

        self.env.add_variable(VarObject(name, value))
        return NilObject()

    def visitFunctionDeclaration(self, ctx:SplikitParser.FunctionDeclarationContext):
        name = ctx.Identifier().getText()
        params = ()
        if ctx.parameterList() is not None:
            params = tuple([identifier.getText() for identifier in ctx.parameterList().Identifier()])

        body = ctx.statement()
        self.env.add_func(FuncObject(name, params, body, None))

    def visitFunctionCall(self, ctx:SplikitParser.FunctionCallContext):
        name = ctx.Identifier().getText()
        if ctx.argumentList() is None:
            args = ()
        else:
            args = tuple([self.visit(expr) for expr in ctx.argumentList().expression()])

        func = self.env.get_func(name)
        return func.call(args, self)

    def visitImportStatement(self, ctx:SplikitParser.ImportStatementContext):
        library = StringObject(ctx.StringLiteral().getText()[1:-1])
        lib = getattr(Libs, library.value)()
        methods = [method for method in dir(lib) if callable(getattr(lib, method)) and not method.startswith('__')]
        for method in methods:
            f = getattr(lib, method)
            self.env.add_func(FuncObject(f.__name__[1:], (), None, f))

    def visitWhileStatement(self, ctx:SplikitParser.WhileStatementContext):
        while self.visit(ctx.expression()):
            for stmt in ctx.statement():
                self.visit(stmt)

    def visitIfStatement(self, ctx:SplikitParser.IfStatementContext):
        stmts = ctx.statement()
        if self.visit(ctx.expression()):
            for stmt in stmts[:-1] if ctx.getText().count('else') >= 1 else stmts:
                self.visit(stmt)
        else:
            for stmt in ctx.statement()[-1:]:
                self.visit(stmt)

    def visitGetAttr(self, ctx:SplikitParser.GetAttrContext):
        obj = self.visit(ctx.primaryExpression())
        attr = ctx.Identifier().getText()
        args = ()
        if ctx.argumentList() is not None:
            args = tuple([self.visit(arg) for arg in ctx.argumentList().expression()])

        if isinstance(obj, ClassObject):
            if f'_{attr}' in obj.methods:
                return obj.methods[f'_{attr}'].call(args, self)
            elif attr in obj.attributes:
                return obj.attributes[attr].value
            else:
                return report_error('Type', f'Unknown attribute \'{attr}\'')

        return getattr(obj, attr)(args)

    def visitExpression(self, ctx:SplikitParser.ExpressionContext):
        if ctx.getAttr() is not None:
            return self.visit(ctx.getAttr())
        elif ctx.operator() is not None:
            if ctx.primaryExpression() is None:
                return

            primary = self.visit(ctx.primaryExpression())
            for i, op in enumerate(ctx.operator()):
                expr2 = self.visit(ctx.expression(i))

                try:
                    p = eval('{}{}{}'.format(primary, op.getText(), expr2))
                    if p is None:
                        return report_error(
                            'Type',
                            f'Invalid types (\'{primary.type}\', \'{expr2.type}\') for operation \'{op.getText()}\''
                        )
                    else:
                        primary = p
                except ValueError:
                    return report_error(
                        'Type',
                        f'Invalid types (\'{primary.type}\', \'{expr2.type}\') for operator {op}'
                    )

            return primary
        elif ctx.getText().startswith('!'):
            return self.visit(ctx.primaryExpression()).__not__()
        elif ctx.primaryExpression() is not None:
            return self.visit(ctx.primaryExpression())

        return NilObject()

    def visitPrimaryExpression(self, ctx:SplikitParser.PrimaryExpressionContext):
        if ctx.atomExpression() is not None:
            return self.visit(ctx.atomExpression())
        elif ctx.expression() is not None:
            return self.visit(ctx.expression())
        elif ctx.functionCall() is not None:
            return self.visit(ctx.functionCall())

    def visitAtomExpression(self, ctx:SplikitParser.AtomExpressionContext):
        if ctx.IntegerLiteral() is not None:
            return IntObject(int(ctx.IntegerLiteral().getText()))
        elif ctx.DecimalLiteral() is not None:
            return FloatObject(float(ctx.DecimalLiteral().getText()))
        elif ctx.StringLiteral() is not None:
            return StringObject(ctx.StringLiteral().getText()[1:-1])
        elif ctx.BooleanLiteral() is not None:
            return BoolObject(bool(ctx.BooleanLiteral().getText().title()))
        elif ctx.argumentList() is not None:
            return ArrayObject([self.visit(arg) for arg in ctx.argumentList().expression()])
        elif ctx.NilLiteral() is not None:
            return NilObject()
        elif ctx.Identifier() is not None:
            if self.env.try_variable(ctx.Identifier().getText()) is not None:
                return self.env.get_variable(ctx.Identifier().getText()).value
            else:
                if self.env.try_func(ctx.Identifier().getText()) is not None:
                    return self.env.get_func(ctx.Identifier().getText())
                else:
                    if self.env.try_cls(ctx.Identifier().getText()) is not None:
                        return self.env.get_cls(ctx.Identifier().getText())
                    else:
                        return report_error('Name', f'Unknown object \'{ctx.Identifier().getText()}\'')
