# Generated from compiler/Splikit.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,185,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,
        3,3,3,57,8,3,1,4,1,4,5,4,61,8,4,10,4,12,4,64,9,4,1,4,1,4,1,5,1,5,
        1,5,1,5,5,5,72,8,5,10,5,12,5,75,9,5,1,5,3,5,78,8,5,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,96,8,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,3,10,105,8,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,12,1,12,1,12,5,12,116,8,12,10,12,12,12,119,9,12,1,13,1,13,
        1,13,1,14,1,14,1,14,5,14,127,8,14,10,14,12,14,130,9,14,1,15,1,15,
        1,15,3,15,135,8,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,3,16,149,8,16,1,17,1,17,1,17,1,17,1,17,3,17,156,8,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,3,17,175,8,17,1,17,3,17,178,8,17,5,17,180,
        8,17,10,17,12,17,183,9,17,1,17,0,1,34,18,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,0,4,1,0,12,13,1,0,14,16,1,0,17,22,1,0,23,
        24,195,0,39,1,0,0,0,2,44,1,0,0,0,4,51,1,0,0,0,6,56,1,0,0,0,8,58,
        1,0,0,0,10,67,1,0,0,0,12,79,1,0,0,0,14,84,1,0,0,0,16,87,1,0,0,0,
        18,91,1,0,0,0,20,104,1,0,0,0,22,110,1,0,0,0,24,112,1,0,0,0,26,120,
        1,0,0,0,28,123,1,0,0,0,30,131,1,0,0,0,32,148,1,0,0,0,34,155,1,0,
        0,0,36,38,3,4,2,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,
        45,5,11,0,0,45,3,1,0,0,0,46,52,3,20,10,0,47,52,3,18,9,0,48,52,3,
        10,5,0,49,52,3,16,8,0,50,52,3,34,17,0,51,46,1,0,0,0,51,47,1,0,0,
        0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,57,3,
        4,2,0,54,55,5,5,0,0,55,57,3,34,17,0,56,53,1,0,0,0,56,54,1,0,0,0,
        57,7,1,0,0,0,58,62,5,31,0,0,59,61,3,6,3,0,60,59,1,0,0,0,61,64,1,
        0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,
        66,5,32,0,0,66,9,1,0,0,0,67,68,5,1,0,0,68,69,3,34,17,0,69,73,3,8,
        4,0,70,72,3,12,6,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,
        74,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,76,78,3,14,7,0,77,76,1,0,
        0,0,77,78,1,0,0,0,78,11,1,0,0,0,79,80,5,2,0,0,80,81,5,1,0,0,81,82,
        3,34,17,0,82,83,3,8,4,0,83,13,1,0,0,0,84,85,5,2,0,0,85,86,3,8,4,
        0,86,15,1,0,0,0,87,88,5,4,0,0,88,89,3,34,17,0,89,90,3,8,4,0,90,17,
        1,0,0,0,91,92,5,3,0,0,92,93,5,11,0,0,93,95,5,29,0,0,94,96,3,28,14,
        0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,30,0,0,98,99,
        5,33,0,0,99,100,3,2,1,0,100,101,1,0,0,0,101,102,3,8,4,0,102,19,1,
        0,0,0,103,105,3,2,1,0,104,103,1,0,0,0,104,105,1,0,0,0,105,106,1,
        0,0,0,106,107,5,11,0,0,107,108,5,28,0,0,108,109,3,34,17,0,109,21,
        1,0,0,0,110,111,3,34,17,0,111,23,1,0,0,0,112,117,3,22,11,0,113,114,
        5,27,0,0,114,116,3,22,11,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,25,1,0,0,0,119,117,1,0,0,0,120,121,3,
        2,1,0,121,122,5,11,0,0,122,27,1,0,0,0,123,128,3,26,13,0,124,125,
        5,27,0,0,125,127,3,26,13,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,
        1,0,0,0,128,129,1,0,0,0,129,29,1,0,0,0,130,128,1,0,0,0,131,132,5,
        11,0,0,132,134,5,29,0,0,133,135,3,24,12,0,134,133,1,0,0,0,134,135,
        1,0,0,0,135,136,1,0,0,0,136,137,5,30,0,0,137,31,1,0,0,0,138,149,
        5,6,0,0,139,149,5,7,0,0,140,149,5,8,0,0,141,149,5,9,0,0,142,149,
        5,10,0,0,143,149,5,11,0,0,144,145,5,29,0,0,145,146,3,34,17,0,146,
        147,5,30,0,0,147,149,1,0,0,0,148,138,1,0,0,0,148,139,1,0,0,0,148,
        140,1,0,0,0,148,141,1,0,0,0,148,142,1,0,0,0,148,143,1,0,0,0,148,
        144,1,0,0,0,149,33,1,0,0,0,150,151,6,17,-1,0,151,156,3,30,15,0,152,
        156,3,32,16,0,153,154,5,25,0,0,154,156,3,34,17,5,155,150,1,0,0,0,
        155,152,1,0,0,0,155,153,1,0,0,0,156,181,1,0,0,0,157,158,10,4,0,0,
        158,159,7,0,0,0,159,180,3,34,17,5,160,161,10,3,0,0,161,162,7,1,0,
        0,162,180,3,34,17,4,163,164,10,2,0,0,164,165,7,2,0,0,165,180,3,34,
        17,3,166,167,10,1,0,0,167,168,7,3,0,0,168,180,3,34,17,2,169,170,
        10,7,0,0,170,171,5,26,0,0,171,177,5,11,0,0,172,174,5,29,0,0,173,
        175,3,24,12,0,174,173,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,
        178,5,30,0,0,177,172,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,
        157,1,0,0,0,179,160,1,0,0,0,179,163,1,0,0,0,179,166,1,0,0,0,179,
        169,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,
        35,1,0,0,0,183,181,1,0,0,0,17,39,51,56,62,73,77,95,104,117,128,134,
        148,155,174,177,179,181
    ]

class SplikitParser ( Parser ):

    grammarFileName = "Splikit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'func'", "'while'", 
                     "'return'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'nil'", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'&&'", "'||'", "'!'", "'.'", "','", "'='", 
                     "'('", "')'", "'{'", "'}'", "'->'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FUNC", "WHILE", "RETURN", 
                      "INT", "FLOAT", "STRING", "BOOL", "NIL", "ID", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EEQ", "NEQ", "GT", "LT", 
                      "GTE", "LTE", "AND", "OR", "NOT", "DOT", "COMMA", 
                      "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "RETURNS", "COMMENT", "WHITESPACE" ]

    RULE_parse = 0
    RULE_type = 1
    RULE_stmt = 2
    RULE_bodyStmts = 3
    RULE_body = 4
    RULE_ifStmt = 5
    RULE_elseifStmt = 6
    RULE_elseStmt = 7
    RULE_whileStmt = 8
    RULE_funcAssign = 9
    RULE_varAssign = 10
    RULE_arg = 11
    RULE_args = 12
    RULE_param = 13
    RULE_params = 14
    RULE_call = 15
    RULE_atom = 16
    RULE_expr = 17

    ruleNames =  [ "parse", "type", "stmt", "bodyStmts", "body", "ifStmt", 
                   "elseifStmt", "elseStmt", "whileStmt", "funcAssign", 
                   "varAssign", "arg", "args", "param", "params", "call", 
                   "atom", "expr" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FUNC=3
    WHILE=4
    RETURN=5
    INT=6
    FLOAT=7
    STRING=8
    BOOL=9
    NIL=10
    ID=11
    ADD=12
    SUB=13
    MUL=14
    DIV=15
    MOD=16
    EEQ=17
    NEQ=18
    GT=19
    LT=20
    GTE=21
    LTE=22
    AND=23
    OR=24
    NOT=25
    DOT=26
    COMMA=27
    ASSIGN=28
    LPAREN=29
    RPAREN=30
    LBRACE=31
    RBRACE=32
    RETURNS=33
    COMMENT=34
    WHITESPACE=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SplikitParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.StmtContext)
            else:
                return self.getTypedRuleContext(SplikitParser.StmtContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_parse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = SplikitParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 570429402) != 0):
                self.state = 36
                self.stmt()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(SplikitParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SplikitParser.ID, 0)

        def getRuleIndex(self):
            return SplikitParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = SplikitParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SplikitParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varAssign(self):
            return self.getTypedRuleContext(SplikitParser.VarAssignContext,0)


        def funcAssign(self):
            return self.getTypedRuleContext(SplikitParser.FuncAssignContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(SplikitParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(SplikitParser.WhileStmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = SplikitParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.varAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.funcAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyStmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(SplikitParser.StmtContext,0)


        def RETURN(self):
            return self.getToken(SplikitParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_bodyStmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyStmts" ):
                return visitor.visitBodyStmts(self)
            else:
                return visitor.visitChildren(self)




    def bodyStmts(self):

        localctx = SplikitParser.BodyStmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bodyStmts)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 6, 7, 8, 9, 10, 11, 25, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.stmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(SplikitParser.RETURN)
                self.state = 55
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SplikitParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SplikitParser.RBRACE, 0)

        def bodyStmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.BodyStmtsContext)
            else:
                return self.getTypedRuleContext(SplikitParser.BodyStmtsContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = SplikitParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(SplikitParser.LBRACE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 570429434) != 0):
                self.state = 59
                self.bodyStmts()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(SplikitParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SplikitParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(SplikitParser.BodyContext,0)


        def elseifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ElseifStmtContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ElseifStmtContext,i)


        def elseStmt(self):
            return self.getTypedRuleContext(SplikitParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = SplikitParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SplikitParser.IF)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.body()
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    self.elseifStmt() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 76
                self.elseStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(SplikitParser.ELSE, 0)

        def IF(self):
            return self.getToken(SplikitParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(SplikitParser.BodyContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_elseifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifStmt" ):
                return visitor.visitElseifStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseifStmt(self):

        localctx = SplikitParser.ElseifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(SplikitParser.ELSE)
            self.state = 80
            self.match(SplikitParser.IF)
            self.state = 81
            self.expr(0)
            self.state = 82
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(SplikitParser.ELSE, 0)

        def body(self):
            return self.getTypedRuleContext(SplikitParser.BodyContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = SplikitParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(SplikitParser.ELSE)
            self.state = 85
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SplikitParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def body(self):
            return self.getTypedRuleContext(SplikitParser.BodyContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = SplikitParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SplikitParser.WHILE)
            self.state = 88
            self.expr(0)
            self.state = 89
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(SplikitParser.FUNC, 0)

        def ID(self):
            return self.getToken(SplikitParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SplikitParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SplikitParser.RPAREN, 0)

        def body(self):
            return self.getTypedRuleContext(SplikitParser.BodyContext,0)


        def RETURNS(self):
            return self.getToken(SplikitParser.RETURNS, 0)

        def type_(self):
            return self.getTypedRuleContext(SplikitParser.TypeContext,0)


        def params(self):
            return self.getTypedRuleContext(SplikitParser.ParamsContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_funcAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncAssign" ):
                return visitor.visitFuncAssign(self)
            else:
                return visitor.visitChildren(self)




    def funcAssign(self):

        localctx = SplikitParser.FuncAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(SplikitParser.FUNC)
            self.state = 92
            self.match(SplikitParser.ID)
            self.state = 93
            self.match(SplikitParser.LPAREN)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 94
                self.params()


            self.state = 97
            self.match(SplikitParser.RPAREN)

            self.state = 98
            self.match(SplikitParser.RETURNS)
            self.state = 99
            self.type_()
            self.state = 101
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SplikitParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(SplikitParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def type_(self):
            return self.getTypedRuleContext(SplikitParser.TypeContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_varAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarAssign" ):
                return visitor.visitVarAssign(self)
            else:
                return visitor.visitChildren(self)




    def varAssign(self):

        localctx = SplikitParser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 103
                self.type_()


            self.state = 106
            self.match(SplikitParser.ID)
            self.state = 107
            self.match(SplikitParser.ASSIGN)
            self.state = 108
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = SplikitParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ArgContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SplikitParser.COMMA)
            else:
                return self.getToken(SplikitParser.COMMA, i)

        def getRuleIndex(self):
            return SplikitParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = SplikitParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.arg()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 113
                self.match(SplikitParser.COMMA)
                self.state = 114
                self.arg()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SplikitParser.TypeContext,0)


        def ID(self):
            return self.getToken(SplikitParser.ID, 0)

        def getRuleIndex(self):
            return SplikitParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = SplikitParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.type_()
            self.state = 121
            self.match(SplikitParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ParamContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SplikitParser.COMMA)
            else:
                return self.getToken(SplikitParser.COMMA, i)

        def getRuleIndex(self):
            return SplikitParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = SplikitParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.param()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 124
                self.match(SplikitParser.COMMA)
                self.state = 125
                self.param()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SplikitParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SplikitParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SplikitParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(SplikitParser.ArgsContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = SplikitParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(SplikitParser.ID)
            self.state = 132
            self.match(SplikitParser.LPAREN)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 570429376) != 0):
                self.state = 133
                self.args()


            self.state = 136
            self.match(SplikitParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SplikitParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SplikitParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(SplikitParser.STRING, 0)

        def BOOL(self):
            return self.getToken(SplikitParser.BOOL, 0)

        def NIL(self):
            return self.getToken(SplikitParser.NIL, 0)

        def ID(self):
            return self.getToken(SplikitParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SplikitParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(SplikitParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(SplikitParser.RPAREN, 0)

        def getRuleIndex(self):
            return SplikitParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = SplikitParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atom)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(SplikitParser.INT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(SplikitParser.FLOAT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(SplikitParser.STRING)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 141
                self.match(SplikitParser.BOOL)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 142
                self.match(SplikitParser.NIL)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.match(SplikitParser.ID)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 7)
                self.state = 144
                self.match(SplikitParser.LPAREN)
                self.state = 145
                self.expr(0)
                self.state = 146
                self.match(SplikitParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def call(self):
            return self.getTypedRuleContext(SplikitParser.CallContext,0)


        def atom(self):
            return self.getTypedRuleContext(SplikitParser.AtomContext,0)


        def NOT(self):
            return self.getToken(SplikitParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ExprContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ExprContext,i)


        def ADD(self):
            return self.getToken(SplikitParser.ADD, 0)

        def SUB(self):
            return self.getToken(SplikitParser.SUB, 0)

        def MUL(self):
            return self.getToken(SplikitParser.MUL, 0)

        def DIV(self):
            return self.getToken(SplikitParser.DIV, 0)

        def MOD(self):
            return self.getToken(SplikitParser.MOD, 0)

        def EEQ(self):
            return self.getToken(SplikitParser.EEQ, 0)

        def NEQ(self):
            return self.getToken(SplikitParser.NEQ, 0)

        def GT(self):
            return self.getToken(SplikitParser.GT, 0)

        def LT(self):
            return self.getToken(SplikitParser.LT, 0)

        def GTE(self):
            return self.getToken(SplikitParser.GTE, 0)

        def LTE(self):
            return self.getToken(SplikitParser.LTE, 0)

        def AND(self):
            return self.getToken(SplikitParser.AND, 0)

        def OR(self):
            return self.getToken(SplikitParser.OR, 0)

        def DOT(self):
            return self.getToken(SplikitParser.DOT, 0)

        def ID(self):
            return self.getToken(SplikitParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SplikitParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SplikitParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(SplikitParser.ArgsContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SplikitParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 151
                self.call()
                pass

            elif la_ == 2:
                self.state = 152
                self.atom()
                pass

            elif la_ == 3:
                self.state = 153
                self.match(SplikitParser.NOT)
                self.state = 154
                self.expr(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 179
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 157
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 158
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 159
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 160
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 161
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 162
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 163
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 164
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 165
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 167
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 168
                        self.expr(2)
                        pass

                    elif la_ == 5:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 170
                        self.match(SplikitParser.DOT)
                        self.state = 171
                        self.match(SplikitParser.ID)
                        self.state = 177
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                        if la_ == 1:
                            self.state = 172
                            self.match(SplikitParser.LPAREN)
                            self.state = 174
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 570429376) != 0):
                                self.state = 173
                                self.args()


                            self.state = 176
                            self.match(SplikitParser.RPAREN)


                        pass

             
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         




