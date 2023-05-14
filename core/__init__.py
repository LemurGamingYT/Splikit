from .gen.SplikitVisitor import SplikitVisitor
from .gen.SplikitParser import SplikitParser
from .env import Environment
from .error import report_error
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
        if ctx.getText().__contains__('::'):
            cls_name = ctx.Identifier(0).getText()
            func_name = ctx.Identifier(1).getText()

            body = ctx.statement()

            params = ()
            if ctx.parameterList() is not None:
                params = tuple([identifier.getText() for identifier in ctx.Identifier(1).Identifier()])

            if self.env.try_cls(cls_name) is not None:
                cls = self.env.get_cls(cls_name)
                cls.methods[func_name] = FuncObject(func_name, params, body, None)
            else:
                return report_error('Name', f'Class \'{cls_name}\' does not exist')
        else:
            name = ctx.Identifier(0).getText()
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

        if self.env.try_cls(name) is not None:
            cls = self.env.get_cls(name)
            init = cls.methods.get('Init')
            if init is not None:
                init.call(args, self)

            return self.env.get_cls(name)

        func = self.env.get_func(name)
        return func.call(args, self)

    def visitImportStatement(self, ctx:SplikitParser.ImportStatementContext):
        as_cls = True if len(ctx.StringLiteral()) == 1 else False

        if as_cls:
            name = ctx.StringLiteral(0).getText()[1:-1]
            lib = getattr(Libs, name)()

            methods = {}
            for method in [method for method in dir(lib) if
                           callable(getattr(lib, method)) and not method.startswith('__')]:
                methods[method] = FuncObject(method, (), None, getattr(lib, method))

            attributes = {}
            for attr in [attr for attr in dir(lib) if not callable(getattr(lib, attr)) and not attr.startswith('__')]:
                attributes[attr] = FuncObject(attr, (), None, getattr(lib, attr))

            obj = ModuleObject(name, attributes, methods)
            obj.__import__(self.env)
        else:
            name = ctx.StringLiteral()[-1].getText()[1:-1]
            lib = getattr(Libs, name)()

            for method in [method for method in dir(lib) if
                           callable(getattr(lib, method)) and not method.startswith('__')]:
                if method in [ident.getText()[1:-1] for ident in ctx.StringLiteral()[:-1]]:
                    self.env.add_func(FuncObject(method, (), None, getattr(lib, method)))

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

    def visitEnumDeclaration(self, ctx:SplikitParser.EnumDeclarationContext):
        enum_name = ctx.Identifier().getText()
        attributes = {}
        for declaration in ctx.variableDeclaration():
            attributes[declaration.Identifier().getText()] = self.visit(declaration.expression())

        self.env.add_cls(ClassObject(enum_name, attributes, {}))

    def visitClassDeclaration(self, ctx:SplikitParser.ClassDeclarationContext):
        name = ctx.Identifier().getText()
        attributes = {}
        methods = {}

        for declaration in ctx.classDeclarations().variableDeclaration():
            attributes[declaration.Identifier().getText()] = self.visit(declaration.expression())

        for func in ctx.classDeclarations().clsFuncDeclaration():
            ident = func.Identifier().getText()

            params = ()
            if func.parameterList() is not None:
                params = tuple([identifier.getText() for identifier in func.parameterList().Identifier()])

            methods[ident] = FuncObject(ident, params, func.statement(), None)

        self.env.add_cls(ClassObject(name, attributes, methods))

    def visitGetAttr(self, ctx:SplikitParser.GetAttrContext):
        obj = self.visit(ctx.primaryExpression())
        attr = ctx.Identifier().getText()
        args = ()
        if ctx.argumentList() is not None:
            args = tuple([self.visit(arg) for arg in ctx.argumentList().expression()])

        if isinstance(obj, ClassObject):
            if attr in obj.methods:
                return obj.methods[attr].call(args, self)
            elif attr in obj.attributes:
                return obj.attributes[attr].value
            else:
                return report_error('Type', f'Unknown attribute \'{attr}\'')
        elif isinstance(obj, ModuleObject):
            if attr in obj.methods:
                return obj.methods[attr].call(args, self)
            elif attr in obj.attributes:
                return obj.attributes[attr].value
            else:
                return report_error('Type', f'Unknown attribute \'{attr}\'')

        return getattr(obj, attr)(args)

    # def visitCastObject(self, ctx:SplikitParser.CastObjectContext):
    #     expr = self.visit(ctx.primaryExpression())
    #     typ = ctx.Identifier().getText()
    #
    #     try:
    #         return getattr(expr, f'As{typ.title()}')()
    #     except AttributeError:
    #         return report_error('Type', f'Invalid cast type \'{expr.type}\' to \'{typ}\'')

    def visitExpression(self, ctx:SplikitParser.ExpressionContext):
        if ctx.operator() is not None:
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
            try:
                return self.visit(ctx.primaryExpression()).__not__()
            except TypeError:
                return report_error('Type',
                                    f'Invalid type \'{self.visit(ctx.primaryExpression()).type}\' for operator \'!\'')
        elif ctx.primaryExpression() is not None:
            return self.visit(ctx.primaryExpression())
        elif ctx.getAttr() is not None:
            return self.visit(ctx.getAttr())
        # elif ctx.castObject() is not None:
        #     return self.visit(ctx.castObject())

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
            name = ctx.Identifier().getText()
            obj = self.env.try_variable(name) or self.env.try_func(name) or self.env.try_cls(
                name) or self.env.try_module(name)
            if obj is not None:
                return obj.value if isinstance(obj, VarObject) else obj
            else:
                return report_error('Name', f'Unknown object \'{name}\'')

