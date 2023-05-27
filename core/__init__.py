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
        idents = [token.getText() for token in ctx.Identifier()]
        if '::' in idents:
            cls_name = idents[0]
            func_name = idents[2]
            params = tuple(ident.getText() for ident in ctx.parameterList().Identifier()) if ctx.parameterList() else ()
            body = ctx.statement()

            if self.env.try_cls(cls_name) is not None:
                cls = self.env.get_cls(cls_name)
                cls.methods[func_name] = FuncObject(func_name, params, body, None)
            else:
                return report_error('Name', f'Class \'{cls_name}\' does not exist')
        else:
            name = idents[0]
            params = tuple(ident.getText() for ident in ctx.parameterList().Identifier()) if ctx.parameterList() else ()
            body = ctx.statement()

            self.env.add_func(FuncObject(name, params, body, None))

    def visitFunctionCall(self, ctx:SplikitParser.FunctionCallContext):
        name = ctx.Identifier().getText()
        args = tuple(self.visit(expr) for expr in ctx.argumentList().expression()) if ctx.argumentList() else ()

        if self.env.try_cls(name) is not None:
            cls = self.env.get_cls(name)
            init = cls.methods.get('Init')
            if init is not None:
                init.call(args, self)

            return self.env.get_cls(name)

        func = self.env.get_func(name)
        return func.call(args, self)

    def visitImportStatement(self, ctx:SplikitParser.ImportStatementContext):
        name = ctx.StringLiteral()[-1].getText()[1:-1]
        try:
            lib = getattr(Libs, name)()
        except AttributeError:
            return report_error('Name', f'Library \'{name}\' was not found')

        methods = {}
        attributes = {}

        if len(ctx.StringLiteral()) == 1:
            for method in dir(lib):
                if callable(getattr(lib, method)) and not method.startswith('__'):
                    methods[method] = FuncObject(method, (), None, getattr(lib, method))
                elif not callable(getattr(lib, method)) and not method.startswith('__'):
                    attributes[method] = FuncObject(method, (), None, getattr(lib, method))
        else:
            for method in dir(lib):
                if callable(getattr(lib, method)) and not method.startswith('__') and method in [ident.getText()[1:-1]
                                                                                                 for ident in
                                                                                                 ctx.StringLiteral()[
                                                                                                 :-1]]:
                    methods[method] = FuncObject(method, (), None, getattr(lib, method))

        obj = ModuleObject(name, attributes, methods)
        obj.__import__(self.env)

    def visitWhileStatement(self, ctx:SplikitParser.WhileStatementContext):
        while self.visit(ctx.expression()):
            for stmt in ctx.statement():
                self.visit(stmt)

    def visitIfStatement(self, ctx: SplikitParser.IfStatementContext):
        stmts = ctx.statement()

        if self.visit(ctx.expression()):
            for stmt in stmts[:-1]:
                self.visit(stmt)
        else:
            for stmt in stmts[-1:]:
                self.visit(stmt)

    def visitEnumDeclaration(self, ctx:SplikitParser.EnumDeclarationContext):
        enum_name = ctx.Identifier().getText()
        attributes = {}
        for declaration in ctx.variableDeclaration():
            attributes[declaration.Identifier().getText()] = self.visit(declaration.expression())

        self.env.add_cls(ClassObject(enum_name, attributes, {}))

    def visitClassDeclaration(self, ctx: SplikitParser.ClassDeclarationContext):
        name = ctx.Identifier().getText()

        attributes = {
            declaration.Identifier().getText(): self.visit(declaration.expression())
            for declaration in ctx.classDeclarations().variableDeclaration()
        }

        methods = {
            func.Identifier().getText(): FuncObject(
                func.Identifier().getText(),
                tuple(identifier.getText() for identifier in
                      func.parameterList().Identifier()) if func.parameterList() is not None else (),
                func.statement(),
                None
            )
            for func in ctx.classDeclarations().clsFuncDeclaration()
        }

        self.env.add_cls(ClassObject(name, attributes, methods))

    def visitGetAttr(self, ctx:SplikitParser.GetAttrContext):
        primary = self.visit(ctx.primaryExpression())

        for i, ident in enumerate([ident.getText() for ident in ctx.Identifier()]):
            args = tuple(self.visit(arg) for arg in ctx.argumentList(i).expression()) if ctx.argumentList(i) else ()

            if isinstance(primary, ClassObject):
                if ident in primary.methods:
                    return primary.methods[ident].call(args, self)
                elif ident in primary.attributes:
                    return primary.attributes[ident]
                else:
                    return report_error('Type', f'Unknown attribute \'{ident}\'')
            elif isinstance(primary, ModuleObject):
                if ident in primary.methods:
                    return primary.methods[ident].call(args, self)
                elif ident in primary.attributes:
                    return primary.attributes[ident]
                else:
                    return report_error('Type', f'Unknown attribute \'{ident}\'')

            primary = getattr(primary, ident)(args, self)
            i += 1

        return primary

    # def visitCastObject(self, ctx:SplikitParser.CastObjectContext):
    #     expr = self.visit(ctx.primaryExpression())
    #     typ = ctx.Identifier().getText()
    #
    #     try:
    #         return getattr(expr, f'As{typ.title()}')()
    #     except AttributeError:
    #         return report_error('Type', f'Invalid cast type \'{expr.type}\' to \'{typ}\'')

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
                    match op.getText():
                        case '+':
                            primary += expr2
                        case '-':
                            primary -= expr2
                        case '*':
                            primary *= expr2
                        case '/':
                            primary /= expr2
                        case '%':
                            primary %= expr2
                        case '==':
                            primary = primary == expr2
                        case '!=':
                            primary = primary != expr2
                        case '<':
                            primary = primary < expr2
                        case '<=':
                            primary = primary <= expr2
                        case '>':
                            primary = primary > expr2
                        case '>=':
                            primary = primary >= expr2
                        case _:
                            return report_error(
                                'Type',
                                f'Invalid operator \'{op.getText()}\''
                            )
                except TypeError:
                    return report_error(
                        'Type',
                        f'Invalid type \'{primary.__type__}\' and \'{expr2.__type__}\' for operator \'{op.getText()}\''
                    )

            return primary

        elif ctx.getText().startswith('!'):
            primary = self.visit(ctx.primaryExpression())

            if not isinstance(primary, BoolObject):
                return report_error(
                    'Type',
                    f'Invalid type \'{primary.type}\' for operator \'!\''
                )

            return primary.__not__()

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
            txt = ctx.BooleanLiteral().getText()
            return BoolObject(True if txt == 'true' else False)
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

