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
        4,1,38,192,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,3,1,3,1,
        3,3,3,57,8,3,1,4,1,4,5,4,61,8,4,10,4,12,4,64,9,4,1,4,1,4,1,5,1,5,
        1,5,1,5,5,5,72,8,5,10,5,12,5,75,9,5,1,5,3,5,78,8,5,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,3,9,93,8,9,1,9,1,9,1,9,1,9,
        3,9,99,8,9,1,9,1,9,1,9,3,9,104,8,9,1,9,1,9,1,10,3,10,109,8,10,1,
        10,3,10,112,8,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,
        12,123,8,12,10,12,12,12,126,9,12,1,13,1,13,1,13,1,14,1,14,1,14,5,
        14,134,8,14,10,14,12,14,137,9,14,1,15,1,15,1,15,3,15,142,8,15,1,
        15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,156,
        8,16,1,17,1,17,1,17,1,17,1,17,3,17,163,8,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        3,17,182,8,17,1,17,3,17,185,8,17,5,17,187,8,17,10,17,12,17,190,9,
        17,1,17,0,1,34,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,0,4,1,0,15,16,1,0,17,19,1,0,20,25,1,0,26,27,205,0,39,1,0,0,0,
        2,44,1,0,0,0,4,51,1,0,0,0,6,56,1,0,0,0,8,58,1,0,0,0,10,67,1,0,0,
        0,12,79,1,0,0,0,14,84,1,0,0,0,16,87,1,0,0,0,18,92,1,0,0,0,20,108,
        1,0,0,0,22,117,1,0,0,0,24,119,1,0,0,0,26,127,1,0,0,0,28,130,1,0,
        0,0,30,138,1,0,0,0,32,155,1,0,0,0,34,162,1,0,0,0,36,38,3,4,2,0,37,
        36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,
        0,41,39,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,45,5,14,0,0,45,3,1,
        0,0,0,46,52,3,20,10,0,47,52,3,18,9,0,48,52,3,10,5,0,49,52,3,16,8,
        0,50,52,3,34,17,0,51,46,1,0,0,0,51,47,1,0,0,0,51,48,1,0,0,0,51,49,
        1,0,0,0,51,50,1,0,0,0,52,5,1,0,0,0,53,57,3,4,2,0,54,55,5,7,0,0,55,
        57,3,34,17,0,56,53,1,0,0,0,56,54,1,0,0,0,57,7,1,0,0,0,58,62,5,34,
        0,0,59,61,3,6,3,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,
        1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,35,0,0,66,9,1,0,0,0,
        67,68,5,1,0,0,68,69,3,34,17,0,69,73,3,8,4,0,70,72,3,12,6,0,71,70,
        1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,77,1,0,0,0,
        75,73,1,0,0,0,76,78,3,14,7,0,77,76,1,0,0,0,77,78,1,0,0,0,78,11,1,
        0,0,0,79,80,5,2,0,0,80,81,5,1,0,0,81,82,3,34,17,0,82,83,3,8,4,0,
        83,13,1,0,0,0,84,85,5,2,0,0,85,86,3,8,4,0,86,15,1,0,0,0,87,88,5,
        5,0,0,88,89,3,34,17,0,89,90,3,8,4,0,90,17,1,0,0,0,91,93,5,6,0,0,
        92,91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,3,0,0,95,96,5,
        14,0,0,96,98,5,32,0,0,97,99,3,28,14,0,98,97,1,0,0,0,98,99,1,0,0,
        0,99,100,1,0,0,0,100,103,5,33,0,0,101,102,5,36,0,0,102,104,3,2,1,
        0,103,101,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,3,8,4,
        0,106,19,1,0,0,0,107,109,5,4,0,0,108,107,1,0,0,0,108,109,1,0,0,0,
        109,111,1,0,0,0,110,112,3,2,1,0,111,110,1,0,0,0,111,112,1,0,0,0,
        112,113,1,0,0,0,113,114,5,14,0,0,114,115,5,31,0,0,115,116,3,34,17,
        0,116,21,1,0,0,0,117,118,3,34,17,0,118,23,1,0,0,0,119,124,3,22,11,
        0,120,121,5,30,0,0,121,123,3,22,11,0,122,120,1,0,0,0,123,126,1,0,
        0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,25,1,0,0,0,126,124,1,0,0,
        0,127,128,3,2,1,0,128,129,5,14,0,0,129,27,1,0,0,0,130,135,3,26,13,
        0,131,132,5,30,0,0,132,134,3,26,13,0,133,131,1,0,0,0,134,137,1,0,
        0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,29,1,0,0,0,137,135,1,0,0,
        0,138,139,5,14,0,0,139,141,5,32,0,0,140,142,3,24,12,0,141,140,1,
        0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,144,5,33,0,0,144,31,1,
        0,0,0,145,156,5,8,0,0,146,156,5,9,0,0,147,156,5,11,0,0,148,156,5,
        12,0,0,149,156,5,13,0,0,150,156,5,14,0,0,151,152,5,32,0,0,152,153,
        3,34,17,0,153,154,5,33,0,0,154,156,1,0,0,0,155,145,1,0,0,0,155,146,
        1,0,0,0,155,147,1,0,0,0,155,148,1,0,0,0,155,149,1,0,0,0,155,150,
        1,0,0,0,155,151,1,0,0,0,156,33,1,0,0,0,157,158,6,17,-1,0,158,163,
        3,30,15,0,159,163,3,32,16,0,160,161,5,28,0,0,161,163,3,34,17,5,162,
        157,1,0,0,0,162,159,1,0,0,0,162,160,1,0,0,0,163,188,1,0,0,0,164,
        165,10,4,0,0,165,166,7,0,0,0,166,187,3,34,17,5,167,168,10,3,0,0,
        168,169,7,1,0,0,169,187,3,34,17,4,170,171,10,2,0,0,171,172,7,2,0,
        0,172,187,3,34,17,3,173,174,10,1,0,0,174,175,7,3,0,0,175,187,3,34,
        17,2,176,177,10,7,0,0,177,178,5,29,0,0,178,184,5,14,0,0,179,181,
        5,32,0,0,180,182,3,24,12,0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,
        1,0,0,0,183,185,5,33,0,0,184,179,1,0,0,0,184,185,1,0,0,0,185,187,
        1,0,0,0,186,164,1,0,0,0,186,167,1,0,0,0,186,170,1,0,0,0,186,173,
        1,0,0,0,186,176,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,
        1,0,0,0,189,35,1,0,0,0,190,188,1,0,0,0,20,39,51,56,62,73,77,92,98,
        103,108,111,124,135,141,155,162,181,184,186,188
    ]

class SplikitParser ( Parser ):

    grammarFileName = "Splikit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'func'", "'const'", 
                     "'while'", "'inline'", "'return'", "<INVALID>", "<INVALID>", 
                     "'''", "<INVALID>", "<INVALID>", "'nil'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "'&&'", "'||'", "'!'", 
                     "'.'", "','", "'='", "'('", "')'", "'{'", "'}'", "'->'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FUNC", "CONST", "WHILE", 
                      "INLINE", "RETURN", "INT", "FLOAT", "APOSTROPHE", 
                      "STRING", "BOOL", "NIL", "ID", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EEQ", "NEQ", "GT", "LT", "GTE", "LTE", 
                      "AND", "OR", "NOT", "DOT", "COMMA", "ASSIGN", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "RETURNS", "COMMENT", 
                      "WHITESPACE" ]

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
    CONST=4
    WHILE=5
    INLINE=6
    RETURN=7
    INT=8
    FLOAT=9
    APOSTROPHE=10
    STRING=11
    BOOL=12
    NIL=13
    ID=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    MOD=19
    EEQ=20
    NEQ=21
    GT=22
    LT=23
    GTE=24
    LTE=25
    AND=26
    OR=27
    NOT=28
    DOT=29
    COMMA=30
    ASSIGN=31
    LPAREN=32
    RPAREN=33
    LBRACE=34
    RBRACE=35
    RETURNS=36
    COMMENT=37
    WHITESPACE=38

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434362) != 0):
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
            if token in [1, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 28, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.stmt()
                pass
            elif token in [7]:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434490) != 0):
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


        def INLINE(self):
            return self.getToken(SplikitParser.INLINE, 0)

        def params(self):
            return self.getTypedRuleContext(SplikitParser.ParamsContext,0)


        def RETURNS(self):
            return self.getToken(SplikitParser.RETURNS, 0)

        def type_(self):
            return self.getTypedRuleContext(SplikitParser.TypeContext,0)


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
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 91
                self.match(SplikitParser.INLINE)


            self.state = 94
            self.match(SplikitParser.FUNC)
            self.state = 95
            self.match(SplikitParser.ID)
            self.state = 96
            self.match(SplikitParser.LPAREN)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 97
                self.params()


            self.state = 100
            self.match(SplikitParser.RPAREN)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 101
                self.match(SplikitParser.RETURNS)
                self.state = 102
                self.type_()


            self.state = 105
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


        def CONST(self):
            return self.getToken(SplikitParser.CONST, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 107
                self.match(SplikitParser.CONST)


            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 110
                self.type_()


            self.state = 113
            self.match(SplikitParser.ID)
            self.state = 114
            self.match(SplikitParser.ASSIGN)
            self.state = 115
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
            self.state = 117
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
            self.state = 119
            self.arg()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 120
                self.match(SplikitParser.COMMA)
                self.state = 121
                self.arg()
                self.state = 126
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
            self.state = 127
            self.type_()
            self.state = 128
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
            self.state = 130
            self.param()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 131
                self.match(SplikitParser.COMMA)
                self.state = 132
                self.param()
                self.state = 137
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
            self.state = 138
            self.match(SplikitParser.ID)
            self.state = 139
            self.match(SplikitParser.LPAREN)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434240) != 0):
                self.state = 140
                self.args()


            self.state = 143
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
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(SplikitParser.INT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(SplikitParser.FLOAT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.match(SplikitParser.STRING)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.match(SplikitParser.BOOL)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.match(SplikitParser.NIL)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.match(SplikitParser.ID)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 7)
                self.state = 151
                self.match(SplikitParser.LPAREN)
                self.state = 152
                self.expr(0)
                self.state = 153
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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 158
                self.call()
                pass

            elif la_ == 2:
                self.state = 159
                self.atom()
                pass

            elif la_ == 3:
                self.state = 160
                self.match(SplikitParser.NOT)
                self.state = 161
                self.expr(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 186
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 165
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 168
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 171
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 172
                        self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 174
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        self.expr(2)
                        pass

                    elif la_ == 5:
                        localctx = SplikitParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 177
                        self.match(SplikitParser.DOT)
                        self.state = 178
                        self.match(SplikitParser.ID)
                        self.state = 184
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                        if la_ == 1:
                            self.state = 179
                            self.match(SplikitParser.LPAREN)
                            self.state = 181
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4563434240) != 0):
                                self.state = 180
                                self.args()


                            self.state = 183
                            self.match(SplikitParser.RPAREN)


                        pass

             
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
         




