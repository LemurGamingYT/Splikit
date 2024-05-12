# Generated from compiler/Splikit.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SplikitParser import SplikitParser
else:
    from SplikitParser import SplikitParser

# This class defines a complete generic visitor for a parse tree produced by SplikitParser.

class SplikitVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SplikitParser#parse.
    def visitParse(self, ctx:SplikitParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#type.
    def visitType(self, ctx:SplikitParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#stmt.
    def visitStmt(self, ctx:SplikitParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#bodyStmts.
    def visitBodyStmts(self, ctx:SplikitParser.BodyStmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#body.
    def visitBody(self, ctx:SplikitParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#ifStmt.
    def visitIfStmt(self, ctx:SplikitParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#elseifStmt.
    def visitElseifStmt(self, ctx:SplikitParser.ElseifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#elseStmt.
    def visitElseStmt(self, ctx:SplikitParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#whileStmt.
    def visitWhileStmt(self, ctx:SplikitParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#foreachStmt.
    def visitForeachStmt(self, ctx:SplikitParser.ForeachStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#useStmt.
    def visitUseStmt(self, ctx:SplikitParser.UseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#funcAssign.
    def visitFuncAssign(self, ctx:SplikitParser.FuncAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#varAssign.
    def visitVarAssign(self, ctx:SplikitParser.VarAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#arg.
    def visitArg(self, ctx:SplikitParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#args.
    def visitArgs(self, ctx:SplikitParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#param.
    def visitParam(self, ctx:SplikitParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#params.
    def visitParams(self, ctx:SplikitParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#call.
    def visitCall(self, ctx:SplikitParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#atom.
    def visitAtom(self, ctx:SplikitParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SplikitParser#expr.
    def visitExpr(self, ctx:SplikitParser.ExprContext):
        return self.visitChildren(ctx)



del SplikitParser