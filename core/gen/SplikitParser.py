# Generated from core/Splikit.g4 by ANTLR 4.13.0
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
        4,1,41,257,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,63,8,3,1,3,1,3,3,3,67,8,3,1,3,1,
        3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,1,3,1,3,1,3,3,3,81,8,3,1,3,
        1,3,1,3,1,3,5,3,87,8,3,10,3,12,3,90,9,3,1,3,3,3,93,8,3,1,4,1,4,1,
        4,1,4,5,4,99,8,4,10,4,12,4,102,9,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,110,
        8,5,1,5,1,5,1,5,5,5,115,8,5,10,5,12,5,118,9,5,1,5,1,5,1,6,1,6,5,
        6,124,8,6,10,6,12,6,127,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        3,8,138,8,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,146,8,9,10,9,12,9,149,9,
        9,1,9,1,9,1,9,1,9,5,9,155,8,9,10,9,12,9,158,9,9,1,9,3,9,161,8,9,
        1,10,1,10,1,10,1,10,1,10,5,10,168,8,10,10,10,12,10,171,9,10,1,10,
        1,10,3,10,175,8,10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,183,8,11,10,
        11,12,11,186,9,11,1,11,1,11,1,12,1,12,1,12,5,12,193,8,12,10,12,12,
        12,196,9,12,1,13,1,13,1,13,5,13,201,8,13,10,13,12,13,204,9,13,1,
        14,1,14,1,14,1,14,1,14,3,14,211,8,14,1,14,3,14,214,8,14,4,14,216,
        8,14,11,14,12,14,217,1,15,1,15,1,15,1,15,5,15,224,8,15,10,15,12,
        15,227,9,15,1,15,1,15,1,15,3,15,232,8,15,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,240,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,
        250,8,17,1,17,3,17,253,8,17,1,18,1,18,1,18,0,0,19,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,0,1,2,0,15,15,19,30,281,0,41,
        1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,92,1,0,0,0,8,94,1,0,0,0,10,105,
        1,0,0,0,12,125,1,0,0,0,14,128,1,0,0,0,16,134,1,0,0,0,18,141,1,0,
        0,0,20,162,1,0,0,0,22,178,1,0,0,0,24,189,1,0,0,0,26,197,1,0,0,0,
        28,205,1,0,0,0,30,231,1,0,0,0,32,239,1,0,0,0,34,252,1,0,0,0,36,254,
        1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,
        41,42,1,0,0,0,42,1,1,0,0,0,43,41,1,0,0,0,44,53,3,4,2,0,45,53,3,6,
        3,0,46,53,3,18,9,0,47,53,3,22,11,0,48,53,3,20,10,0,49,53,3,8,4,0,
        50,53,3,14,7,0,51,53,3,30,15,0,52,44,1,0,0,0,52,45,1,0,0,0,52,46,
        1,0,0,0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,
        52,51,1,0,0,0,53,3,1,0,0,0,54,55,5,39,0,0,55,56,5,1,0,0,56,57,3,
        30,15,0,57,5,1,0,0,0,58,59,5,2,0,0,59,62,5,39,0,0,60,61,5,3,0,0,
        61,63,5,39,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,66,5,
        4,0,0,65,67,3,24,12,0,66,65,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,
        68,69,5,5,0,0,69,73,5,6,0,0,70,72,3,2,1,0,71,70,1,0,0,0,72,75,1,
        0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,
        93,5,7,0,0,77,78,5,39,0,0,78,80,5,4,0,0,79,81,3,24,12,0,80,79,1,
        0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,5,0,0,83,84,5,8,0,0,84,
        88,5,6,0,0,85,87,3,2,1,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,
        0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,93,5,7,0,0,92,58,
        1,0,0,0,92,77,1,0,0,0,93,7,1,0,0,0,94,95,5,9,0,0,95,96,5,39,0,0,
        96,100,5,6,0,0,97,99,3,4,2,0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,
        1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,
        5,7,0,0,104,9,1,0,0,0,105,106,5,2,0,0,106,107,5,39,0,0,107,109,5,
        4,0,0,108,110,3,24,12,0,109,108,1,0,0,0,109,110,1,0,0,0,110,111,
        1,0,0,0,111,112,5,5,0,0,112,116,5,6,0,0,113,115,3,2,1,0,114,113,
        1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,119,
        1,0,0,0,118,116,1,0,0,0,119,120,5,7,0,0,120,11,1,0,0,0,121,124,3,
        10,5,0,122,124,3,4,2,0,123,121,1,0,0,0,123,122,1,0,0,0,124,127,1,
        0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,13,1,0,0,0,127,125,1,0,
        0,0,128,129,5,10,0,0,129,130,5,39,0,0,130,131,5,6,0,0,131,132,3,
        12,6,0,132,133,5,7,0,0,133,15,1,0,0,0,134,135,5,39,0,0,135,137,5,
        4,0,0,136,138,3,26,13,0,137,136,1,0,0,0,137,138,1,0,0,0,138,139,
        1,0,0,0,139,140,5,5,0,0,140,17,1,0,0,0,141,142,5,11,0,0,142,143,
        3,30,15,0,143,147,5,6,0,0,144,146,3,2,1,0,145,144,1,0,0,0,146,149,
        1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,147,
        1,0,0,0,150,160,5,7,0,0,151,152,5,12,0,0,152,156,5,6,0,0,153,155,
        3,2,1,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,
        1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,161,5,7,0,0,160,151,
        1,0,0,0,160,161,1,0,0,0,161,19,1,0,0,0,162,174,5,13,0,0,163,164,
        5,6,0,0,164,169,5,34,0,0,165,166,5,14,0,0,166,168,5,34,0,0,167,165,
        1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,172,
        1,0,0,0,171,169,1,0,0,0,172,175,5,7,0,0,173,175,5,15,0,0,174,163,
        1,0,0,0,174,173,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,
        5,34,0,0,177,21,1,0,0,0,178,179,5,16,0,0,179,180,3,30,15,0,180,184,
        5,6,0,0,181,183,3,2,1,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,
        1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,188,
        5,7,0,0,188,23,1,0,0,0,189,194,5,39,0,0,190,191,5,14,0,0,191,193,
        5,39,0,0,192,190,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,
        1,0,0,0,195,25,1,0,0,0,196,194,1,0,0,0,197,202,3,30,15,0,198,199,
        5,14,0,0,199,201,3,30,15,0,200,198,1,0,0,0,201,204,1,0,0,0,202,200,
        1,0,0,0,202,203,1,0,0,0,203,27,1,0,0,0,204,202,1,0,0,0,205,215,3,
        32,16,0,206,207,5,17,0,0,207,213,5,39,0,0,208,210,5,4,0,0,209,211,
        3,26,13,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,214,
        5,5,0,0,213,208,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,206,
        1,0,0,0,216,217,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,29,1,
        0,0,0,219,225,3,32,16,0,220,221,3,36,18,0,221,222,3,30,15,0,222,
        224,1,0,0,0,223,220,1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,
        226,1,0,0,0,226,232,1,0,0,0,227,225,1,0,0,0,228,229,5,18,0,0,229,
        232,3,32,16,0,230,232,3,28,14,0,231,219,1,0,0,0,231,228,1,0,0,0,
        231,230,1,0,0,0,232,31,1,0,0,0,233,234,5,4,0,0,234,235,3,30,15,0,
        235,236,5,5,0,0,236,240,1,0,0,0,237,240,3,16,8,0,238,240,3,34,17,
        0,239,233,1,0,0,0,239,237,1,0,0,0,239,238,1,0,0,0,240,33,1,0,0,0,
        241,253,5,31,0,0,242,253,5,32,0,0,243,253,5,34,0,0,244,253,5,35,
        0,0,245,253,5,36,0,0,246,253,5,39,0,0,247,249,5,6,0,0,248,250,3,
        26,13,0,249,248,1,0,0,0,249,250,1,0,0,0,250,251,1,0,0,0,251,253,
        5,7,0,0,252,241,1,0,0,0,252,242,1,0,0,0,252,243,1,0,0,0,252,244,
        1,0,0,0,252,245,1,0,0,0,252,246,1,0,0,0,252,247,1,0,0,0,253,35,1,
        0,0,0,254,255,7,0,0,0,255,37,1,0,0,0,30,41,52,62,66,73,80,88,92,
        100,109,116,123,125,137,147,156,160,169,174,184,194,202,210,213,
        217,225,231,239,249,252
    ]

class SplikitParser ( Parser ):

    grammarFileName = "Splikit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'func'", "'::'", "'('", "')'", 
                     "'{'", "'}'", "'=>'", "'enum'", "'class'", "'if'", 
                     "'else'", "'import'", "','", "'*'", "'while'", "'.'", 
                     "'!'", "'+'", "'-'", "'/'", "'%'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'&'", "'|'", "<INVALID>", 
                     "<INVALID>", "'''", "<INVALID>", "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IntegerLiteral", 
                      "DecimalLiteral", "Apostrophe", "StringLiteral", "BooleanLiteral", 
                      "NilLiteral", "Comment", "MultiLineComment", "Identifier", 
                      "Digit", "Whitespace" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_functionDeclaration = 3
    RULE_enumDeclaration = 4
    RULE_clsFuncDeclaration = 5
    RULE_classDeclarations = 6
    RULE_classDeclaration = 7
    RULE_functionCall = 8
    RULE_ifStatement = 9
    RULE_importStatement = 10
    RULE_whileStatement = 11
    RULE_parameterList = 12
    RULE_argumentList = 13
    RULE_getAttr = 14
    RULE_expression = 15
    RULE_primaryExpression = 16
    RULE_atomExpression = 17
    RULE_operator = 18

    ruleNames =  [ "program", "statement", "variableDeclaration", "functionDeclaration", 
                   "enumDeclaration", "clsFuncDeclaration", "classDeclarations", 
                   "classDeclaration", "functionCall", "ifStatement", "importStatement", 
                   "whileStatement", "parameterList", "argumentList", "getAttr", 
                   "expression", "primaryExpression", "atomExpression", 
                   "operator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    IntegerLiteral=31
    DecimalLiteral=32
    Apostrophe=33
    StringLiteral=34
    BooleanLiteral=35
    NilLiteral=36
    Comment=37
    MultiLineComment=38
    Identifier=39
    Digit=40
    Whitespace=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.StatementContext)
            else:
                return self.getTypedRuleContext(SplikitParser.StatementContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SplikitParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688660) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(SplikitParser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(SplikitParser.FunctionDeclarationContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SplikitParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(SplikitParser.WhileStatementContext,0)


        def importStatement(self):
            return self.getTypedRuleContext(SplikitParser.ImportStatementContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(SplikitParser.EnumDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(SplikitParser.ClassDeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(SplikitParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SplikitParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.functionDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.importStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.enumDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.classDeclaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 51
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SplikitParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(SplikitParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = SplikitParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SplikitParser.Identifier)
            self.state = 55
            self.match(SplikitParser.T__0)
            self.state = 56
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(SplikitParser.Identifier)
            else:
                return self.getToken(SplikitParser.Identifier, i)

        def parameterList(self):
            return self.getTypedRuleContext(SplikitParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.StatementContext)
            else:
                return self.getTypedRuleContext(SplikitParser.StatementContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = SplikitParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(SplikitParser.T__1)
                self.state = 59
                self.match(SplikitParser.Identifier)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 60
                    self.match(SplikitParser.T__2)
                    self.state = 61
                    self.match(SplikitParser.Identifier)


                self.state = 64
                self.match(SplikitParser.T__3)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 65
                    self.parameterList()


                self.state = 68
                self.match(SplikitParser.T__4)
                self.state = 69
                self.match(SplikitParser.T__5)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688660) != 0):
                    self.state = 70
                    self.statement()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 76
                self.match(SplikitParser.T__6)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(SplikitParser.Identifier)
                self.state = 78
                self.match(SplikitParser.T__3)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 79
                    self.parameterList()


                self.state = 82
                self.match(SplikitParser.T__4)
                self.state = 83
                self.match(SplikitParser.T__7)
                self.state = 84
                self.match(SplikitParser.T__5)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688660) != 0):
                    self.state = 85
                    self.statement()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 91
                self.match(SplikitParser.T__6)
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


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SplikitParser.Identifier, 0)

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(SplikitParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_enumDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDeclaration" ):
                return visitor.visitEnumDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumDeclaration(self):

        localctx = SplikitParser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(SplikitParser.T__8)
            self.state = 95
            self.match(SplikitParser.Identifier)
            self.state = 96
            self.match(SplikitParser.T__5)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 97
                self.variableDeclaration()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(SplikitParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClsFuncDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SplikitParser.Identifier, 0)

        def parameterList(self):
            return self.getTypedRuleContext(SplikitParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.StatementContext)
            else:
                return self.getTypedRuleContext(SplikitParser.StatementContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_clsFuncDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClsFuncDeclaration" ):
                return visitor.visitClsFuncDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def clsFuncDeclaration(self):

        localctx = SplikitParser.ClsFuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_clsFuncDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(SplikitParser.T__1)
            self.state = 106
            self.match(SplikitParser.Identifier)
            self.state = 107
            self.match(SplikitParser.T__3)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 108
                self.parameterList()


            self.state = 111
            self.match(SplikitParser.T__4)
            self.state = 112
            self.match(SplikitParser.T__5)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688660) != 0):
                self.state = 113
                self.statement()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(SplikitParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clsFuncDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ClsFuncDeclarationContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ClsFuncDeclarationContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(SplikitParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_classDeclarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclarations" ):
                return visitor.visitClassDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def classDeclarations(self):

        localctx = SplikitParser.ClassDeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_classDeclarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==39:
                self.state = 123
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 121
                    self.clsFuncDeclaration()
                    pass
                elif token in [39]:
                    self.state = 122
                    self.variableDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SplikitParser.Identifier, 0)

        def classDeclarations(self):
            return self.getTypedRuleContext(SplikitParser.ClassDeclarationsContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_classDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = SplikitParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_classDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(SplikitParser.T__9)
            self.state = 129
            self.match(SplikitParser.Identifier)
            self.state = 130
            self.match(SplikitParser.T__5)
            self.state = 131
            self.classDeclarations()
            self.state = 132
            self.match(SplikitParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SplikitParser.Identifier, 0)

        def argumentList(self):
            return self.getTypedRuleContext(SplikitParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = SplikitParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(SplikitParser.Identifier)
            self.state = 135
            self.match(SplikitParser.T__3)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457611344) != 0):
                self.state = 136
                self.argumentList()


            self.state = 139
            self.match(SplikitParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SplikitParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.StatementContext)
            else:
                return self.getTypedRuleContext(SplikitParser.StatementContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = SplikitParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(SplikitParser.T__10)
            self.state = 142
            self.expression()
            self.state = 143
            self.match(SplikitParser.T__5)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688660) != 0):
                self.state = 144
                self.statement()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(SplikitParser.T__6)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 151
                self.match(SplikitParser.T__11)
                self.state = 152
                self.match(SplikitParser.T__5)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688660) != 0):
                    self.state = 153
                    self.statement()
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 159
                self.match(SplikitParser.T__6)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(SplikitParser.StringLiteral)
            else:
                return self.getToken(SplikitParser.StringLiteral, i)

        def getRuleIndex(self):
            return SplikitParser.RULE_importStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStatement" ):
                return visitor.visitImportStatement(self)
            else:
                return visitor.visitChildren(self)




    def importStatement(self):

        localctx = SplikitParser.ImportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_importStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(SplikitParser.T__12)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 163
                self.match(SplikitParser.T__5)
                self.state = 164
                self.match(SplikitParser.StringLiteral)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 165
                    self.match(SplikitParser.T__13)
                    self.state = 166
                    self.match(SplikitParser.StringLiteral)
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 172
                self.match(SplikitParser.T__6)
                pass
            elif token in [15]:
                self.state = 173
                self.match(SplikitParser.T__14)
                pass
            elif token in [34]:
                pass
            else:
                pass
            self.state = 176
            self.match(SplikitParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SplikitParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.StatementContext)
            else:
                return self.getTypedRuleContext(SplikitParser.StatementContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = SplikitParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(SplikitParser.T__15)
            self.state = 179
            self.expression()
            self.state = 180
            self.match(SplikitParser.T__5)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688660) != 0):
                self.state = 181
                self.statement()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(SplikitParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(SplikitParser.Identifier)
            else:
                return self.getToken(SplikitParser.Identifier, i)

        def getRuleIndex(self):
            return SplikitParser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = SplikitParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(SplikitParser.Identifier)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 190
                self.match(SplikitParser.T__13)
                self.state = 191
                self.match(SplikitParser.Identifier)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = SplikitParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expression()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 198
                self.match(SplikitParser.T__13)
                self.state = 199
                self.expression()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(SplikitParser.PrimaryExpressionContext,0)


        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(SplikitParser.Identifier)
            else:
                return self.getToken(SplikitParser.Identifier, i)

        def argumentList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ArgumentListContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ArgumentListContext,i)


        def getRuleIndex(self):
            return SplikitParser.RULE_getAttr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetAttr" ):
                return visitor.visitGetAttr(self)
            else:
                return visitor.visitChildren(self)




    def getAttr(self):

        localctx = SplikitParser.GetAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_getAttr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.primaryExpression()
            self.state = 215 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 206
                self.match(SplikitParser.T__16)
                self.state = 207
                self.match(SplikitParser.Identifier)
                self.state = 213
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 208
                    self.match(SplikitParser.T__3)
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457611344) != 0):
                        self.state = 209
                        self.argumentList()


                    self.state = 212
                    self.match(SplikitParser.T__4)


                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==17):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(SplikitParser.PrimaryExpressionContext,0)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.OperatorContext)
            else:
                return self.getTypedRuleContext(SplikitParser.OperatorContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SplikitParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SplikitParser.ExpressionContext,i)


        def getAttr(self):
            return self.getTypedRuleContext(SplikitParser.GetAttrContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SplikitParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.primaryExpression()
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 220
                        self.operator()
                        self.state = 221
                        self.expression() 
                    self.state = 227
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(SplikitParser.T__17)
                self.state = 229
                self.primaryExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.getAttr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SplikitParser.ExpressionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SplikitParser.FunctionCallContext,0)


        def atomExpression(self):
            return self.getTypedRuleContext(SplikitParser.AtomExpressionContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_primaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = SplikitParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_primaryExpression)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(SplikitParser.T__3)
                self.state = 234
                self.expression()
                self.state = 235
                self.match(SplikitParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.atomExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(SplikitParser.IntegerLiteral, 0)

        def DecimalLiteral(self):
            return self.getToken(SplikitParser.DecimalLiteral, 0)

        def StringLiteral(self):
            return self.getToken(SplikitParser.StringLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(SplikitParser.BooleanLiteral, 0)

        def NilLiteral(self):
            return self.getToken(SplikitParser.NilLiteral, 0)

        def Identifier(self):
            return self.getToken(SplikitParser.Identifier, 0)

        def argumentList(self):
            return self.getTypedRuleContext(SplikitParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return SplikitParser.RULE_atomExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpression" ):
                return visitor.visitAtomExpression(self)
            else:
                return visitor.visitChildren(self)




    def atomExpression(self):

        localctx = SplikitParser.AtomExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_atomExpression)
        self._la = 0 # Token type
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(SplikitParser.IntegerLiteral)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(SplikitParser.DecimalLiteral)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.match(SplikitParser.StringLiteral)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.match(SplikitParser.BooleanLiteral)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 245
                self.match(SplikitParser.NilLiteral)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 246
                self.match(SplikitParser.Identifier)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 247
                self.match(SplikitParser.T__5)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457611344) != 0):
                    self.state = 248
                    self.argumentList()


                self.state = 251
                self.match(SplikitParser.T__6)
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


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SplikitParser.RULE_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = SplikitParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2146992128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





