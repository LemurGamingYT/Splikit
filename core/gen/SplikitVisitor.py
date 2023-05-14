# Generated from core/Splikit.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SplikitParser import SplikitParser
else:
    from SplikitParser import SplikitParser

# This class defines a complete generic visitor for a parse tree produced by SplikitParser.

class SplikitVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SplikitParser#program.
    def visitProgram(self, ctx:SplikitParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#statement.
    def visitStatement(self, ctx:SplikitParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SplikitParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:SplikitParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:SplikitParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#clsFuncDeclaration.
    def visitClsFuncDeclaration(self, ctx:SplikitParser.ClsFuncDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#classDeclarations.
    def visitClassDeclarations(self, ctx:SplikitParser.ClassDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#classDeclaration.
    def visitClassDeclaration(self, ctx:SplikitParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#functionCall.
    def visitFunctionCall(self, ctx:SplikitParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#ifStatement.
    def visitIfStatement(self, ctx:SplikitParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#importStatement.
    def visitImportStatement(self, ctx:SplikitParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#whileStatement.
    def visitWhileStatement(self, ctx:SplikitParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#parameterList.
    def visitParameterList(self, ctx:SplikitParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#argumentList.
    def visitArgumentList(self, ctx:SplikitParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#getAttr.
    def visitGetAttr(self, ctx:SplikitParser.GetAttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#expression.
    def visitExpression(self, ctx:SplikitParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:SplikitParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#atomExpression.
    def visitAtomExpression(self, ctx:SplikitParser.AtomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#operator.
    def visitOperator(self, ctx:SplikitParser.OperatorContext):
        return self.visitChildren(ctx)



del SplikitParser