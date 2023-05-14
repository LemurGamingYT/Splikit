# Generated from core/Splikit.g4 by ANTLR 4.12.0
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
        4,1,41,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,63,8,3,1,3,1,3,1,3,5,3,68,8,3,10,
        3,12,3,71,9,3,1,3,1,3,1,3,1,3,3,3,77,8,3,1,3,1,3,1,3,1,3,5,3,83,
        8,3,10,3,12,3,86,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,95,8,3,1,3,
        1,3,1,3,5,3,100,8,3,10,3,12,3,103,9,3,1,3,3,3,106,8,3,1,4,1,4,1,
        4,1,4,5,4,112,8,4,10,4,12,4,115,9,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,
        123,8,5,1,5,1,5,1,5,5,5,128,8,5,10,5,12,5,131,9,5,1,5,1,5,1,6,5,
        6,136,8,6,10,6,12,6,139,9,6,1,6,5,6,142,8,6,10,6,12,6,145,9,6,3,
        6,147,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,158,8,8,1,8,1,
        8,1,9,1,9,1,9,1,9,5,9,166,8,9,10,9,12,9,169,9,9,1,9,1,9,1,9,1,9,
        5,9,175,8,9,10,9,12,9,178,9,9,1,9,3,9,181,8,9,1,10,1,10,1,10,1,10,
        1,10,5,10,188,8,10,10,10,12,10,191,9,10,1,10,1,10,3,10,195,8,10,
        1,10,1,10,1,11,1,11,1,11,1,11,5,11,203,8,11,10,11,12,11,206,9,11,
        1,11,1,11,1,12,1,12,1,12,5,12,213,8,12,10,12,12,12,216,9,12,1,13,
        1,13,1,13,5,13,221,8,13,10,13,12,13,224,9,13,1,14,1,14,1,14,1,14,
        1,14,3,14,231,8,14,1,14,3,14,234,8,14,1,15,1,15,1,15,1,15,5,15,240,
        8,15,10,15,12,15,243,9,15,1,15,1,15,1,15,3,15,248,8,15,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,256,8,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,3,17,266,8,17,1,17,3,17,269,8,17,1,18,1,18,1,18,0,0,19,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,1,2,0,15,15,
        19,30,299,0,41,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,105,1,0,0,0,8,
        107,1,0,0,0,10,118,1,0,0,0,12,146,1,0,0,0,14,148,1,0,0,0,16,154,
        1,0,0,0,18,161,1,0,0,0,20,182,1,0,0,0,22,198,1,0,0,0,24,209,1,0,
        0,0,26,217,1,0,0,0,28,225,1,0,0,0,30,247,1,0,0,0,32,255,1,0,0,0,
        34,268,1,0,0,0,36,270,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,1,1,0,0,0,43,41,1,0,0,0,44,
        53,3,4,2,0,45,53,3,6,3,0,46,53,3,18,9,0,47,53,3,22,11,0,48,53,3,
        20,10,0,49,53,3,8,4,0,50,53,3,14,7,0,51,53,3,30,15,0,52,44,1,0,0,
        0,52,45,1,0,0,0,52,46,1,0,0,0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,
        1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,3,1,0,0,0,54,55,5,39,0,0,
        55,56,5,1,0,0,56,57,3,30,15,0,57,5,1,0,0,0,58,59,5,2,0,0,59,60,5,
        39,0,0,60,62,5,3,0,0,61,63,3,24,12,0,62,61,1,0,0,0,62,63,1,0,0,0,
        63,64,1,0,0,0,64,65,5,4,0,0,65,69,5,5,0,0,66,68,3,2,1,0,67,66,1,
        0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,
        69,1,0,0,0,72,106,5,6,0,0,73,74,5,39,0,0,74,76,5,3,0,0,75,77,3,24,
        12,0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,5,4,0,0,79,
        80,5,7,0,0,80,84,5,5,0,0,81,83,3,2,1,0,82,81,1,0,0,0,83,86,1,0,0,
        0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,87,106,
        5,6,0,0,88,89,5,2,0,0,89,90,5,39,0,0,90,91,5,8,0,0,91,92,5,39,0,
        0,92,94,5,3,0,0,93,95,3,24,12,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,
        1,0,0,0,96,97,5,4,0,0,97,101,5,5,0,0,98,100,3,2,1,0,99,98,1,0,0,
        0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,
        103,101,1,0,0,0,104,106,5,6,0,0,105,58,1,0,0,0,105,73,1,0,0,0,105,
        88,1,0,0,0,106,7,1,0,0,0,107,108,5,9,0,0,108,109,5,39,0,0,109,113,
        5,5,0,0,110,112,3,4,2,0,111,110,1,0,0,0,112,115,1,0,0,0,113,111,
        1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,117,
        5,6,0,0,117,9,1,0,0,0,118,119,5,2,0,0,119,120,5,39,0,0,120,122,5,
        3,0,0,121,123,3,24,12,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,
        1,0,0,0,124,125,5,4,0,0,125,129,5,5,0,0,126,128,3,2,1,0,127,126,
        1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,
        1,0,0,0,131,129,1,0,0,0,132,133,5,6,0,0,133,11,1,0,0,0,134,136,3,
        10,5,0,135,134,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,
        0,0,0,138,147,1,0,0,0,139,137,1,0,0,0,140,142,3,4,2,0,141,140,1,
        0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,147,1,
        0,0,0,145,143,1,0,0,0,146,137,1,0,0,0,146,143,1,0,0,0,147,13,1,0,
        0,0,148,149,5,10,0,0,149,150,5,39,0,0,150,151,5,5,0,0,151,152,3,
        12,6,0,152,153,5,6,0,0,153,15,1,0,0,0,154,155,5,39,0,0,155,157,5,
        3,0,0,156,158,3,26,13,0,157,156,1,0,0,0,157,158,1,0,0,0,158,159,
        1,0,0,0,159,160,5,4,0,0,160,17,1,0,0,0,161,162,5,11,0,0,162,163,
        3,30,15,0,163,167,5,5,0,0,164,166,3,2,1,0,165,164,1,0,0,0,166,169,
        1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,
        1,0,0,0,170,180,5,6,0,0,171,172,5,12,0,0,172,176,5,5,0,0,173,175,
        3,2,1,0,174,173,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,
        1,0,0,0,177,179,1,0,0,0,178,176,1,0,0,0,179,181,5,6,0,0,180,171,
        1,0,0,0,180,181,1,0,0,0,181,19,1,0,0,0,182,194,5,13,0,0,183,184,
        5,5,0,0,184,189,5,34,0,0,185,186,5,14,0,0,186,188,5,34,0,0,187,185,
        1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,192,
        1,0,0,0,191,189,1,0,0,0,192,195,5,6,0,0,193,195,5,15,0,0,194,183,
        1,0,0,0,194,193,1,0,0,0,194,195,1,0,0,0,195,196,1,0,0,0,196,197,
        5,34,0,0,197,21,1,0,0,0,198,199,5,16,0,0,199,200,3,30,15,0,200,204,
        5,5,0,0,201,203,3,2,1,0,202,201,1,0,0,0,203,206,1,0,0,0,204,202,
        1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,204,1,0,0,0,207,208,
        5,6,0,0,208,23,1,0,0,0,209,214,5,39,0,0,210,211,5,14,0,0,211,213,
        5,39,0,0,212,210,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,
        1,0,0,0,215,25,1,0,0,0,216,214,1,0,0,0,217,222,3,30,15,0,218,219,
        5,14,0,0,219,221,3,30,15,0,220,218,1,0,0,0,221,224,1,0,0,0,222,220,
        1,0,0,0,222,223,1,0,0,0,223,27,1,0,0,0,224,222,1,0,0,0,225,226,3,
        32,16,0,226,227,5,17,0,0,227,233,5,39,0,0,228,230,5,3,0,0,229,231,
        3,26,13,0,230,229,1,0,0,0,230,231,1,0,0,0,231,232,1,0,0,0,232,234,
        5,4,0,0,233,228,1,0,0,0,233,234,1,0,0,0,234,29,1,0,0,0,235,241,3,
        32,16,0,236,237,3,36,18,0,237,238,3,30,15,0,238,240,1,0,0,0,239,
        236,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,
        248,1,0,0,0,243,241,1,0,0,0,244,245,5,18,0,0,245,248,3,32,16,0,246,
        248,3,28,14,0,247,235,1,0,0,0,247,244,1,0,0,0,247,246,1,0,0,0,248,
        31,1,0,0,0,249,250,5,3,0,0,250,251,3,30,15,0,251,252,5,4,0,0,252,
        256,1,0,0,0,253,256,3,16,8,0,254,256,3,34,17,0,255,249,1,0,0,0,255,
        253,1,0,0,0,255,254,1,0,0,0,256,33,1,0,0,0,257,269,5,31,0,0,258,
        269,5,32,0,0,259,269,5,34,0,0,260,269,5,35,0,0,261,269,5,36,0,0,
        262,269,5,39,0,0,263,265,5,5,0,0,264,266,3,26,13,0,265,264,1,0,0,
        0,265,266,1,0,0,0,266,267,1,0,0,0,267,269,5,6,0,0,268,257,1,0,0,
        0,268,258,1,0,0,0,268,259,1,0,0,0,268,260,1,0,0,0,268,261,1,0,0,
        0,268,262,1,0,0,0,268,263,1,0,0,0,269,35,1,0,0,0,270,271,7,0,0,0,
        271,37,1,0,0,0,31,41,52,62,69,76,84,94,101,105,113,122,129,137,143,
        146,157,167,176,180,189,194,204,214,222,230,233,241,247,255,265,
        268
    ]

class SplikitParser ( Parser ):

    grammarFileName = "Splikit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'func'", "'('", "')'", "'{'", 
                     "'}'", "'=>'", "'::'", "'enum'", "'class'", "'if'", 
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
        self.checkVersion("4.12.0")
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(SplikitParser.T__1)
                self.state = 59
                self.match(SplikitParser.Identifier)
                self.state = 60
                self.match(SplikitParser.T__2)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 61
                    self.parameterList()


                self.state = 64
                self.match(SplikitParser.T__3)
                self.state = 65
                self.match(SplikitParser.T__4)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
                    self.state = 66
                    self.statement()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(SplikitParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(SplikitParser.Identifier)
                self.state = 74
                self.match(SplikitParser.T__2)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 75
                    self.parameterList()


                self.state = 78
                self.match(SplikitParser.T__3)
                self.state = 79
                self.match(SplikitParser.T__6)
                self.state = 80
                self.match(SplikitParser.T__4)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
                    self.state = 81
                    self.statement()
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.match(SplikitParser.T__5)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(SplikitParser.T__1)
                self.state = 89
                self.match(SplikitParser.Identifier)
                self.state = 90
                self.match(SplikitParser.T__7)
                self.state = 91
                self.match(SplikitParser.Identifier)
                self.state = 92
                self.match(SplikitParser.T__2)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 93
                    self.parameterList()


                self.state = 96
                self.match(SplikitParser.T__3)
                self.state = 97
                self.match(SplikitParser.T__4)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
                    self.state = 98
                    self.statement()
                    self.state = 103
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 104
                self.match(SplikitParser.T__5)
                pass


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
            self.state = 107
            self.match(SplikitParser.T__8)
            self.state = 108
            self.match(SplikitParser.Identifier)
            self.state = 109
            self.match(SplikitParser.T__4)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 110
                self.variableDeclaration()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(SplikitParser.T__5)
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
            self.state = 118
            self.match(SplikitParser.T__1)
            self.state = 119
            self.match(SplikitParser.Identifier)
            self.state = 120
            self.match(SplikitParser.T__2)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 121
                self.parameterList()


            self.state = 124
            self.match(SplikitParser.T__3)
            self.state = 125
            self.match(SplikitParser.T__4)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
                self.state = 126
                self.statement()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(SplikitParser.T__5)
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
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 134
                    self.clsFuncDeclaration()
                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 140
                    self.variableDeclaration()
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


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
            self.state = 148
            self.match(SplikitParser.T__9)
            self.state = 149
            self.match(SplikitParser.Identifier)
            self.state = 150
            self.match(SplikitParser.T__4)
            self.state = 151
            self.classDeclarations()
            self.state = 152
            self.match(SplikitParser.T__5)
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
            self.state = 154
            self.match(SplikitParser.Identifier)
            self.state = 155
            self.match(SplikitParser.T__2)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457611304) != 0):
                self.state = 156
                self.argumentList()


            self.state = 159
            self.match(SplikitParser.T__3)
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
            self.state = 161
            self.match(SplikitParser.T__10)
            self.state = 162
            self.expression()
            self.state = 163
            self.match(SplikitParser.T__4)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
                self.state = 164
                self.statement()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(SplikitParser.T__5)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 171
                self.match(SplikitParser.T__11)
                self.state = 172
                self.match(SplikitParser.T__4)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
                    self.state = 173
                    self.statement()
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 179
                self.match(SplikitParser.T__5)


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
            self.state = 182
            self.match(SplikitParser.T__12)
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 183
                self.match(SplikitParser.T__4)
                self.state = 184
                self.match(SplikitParser.StringLiteral)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 185
                    self.match(SplikitParser.T__13)
                    self.state = 186
                    self.match(SplikitParser.StringLiteral)
                    self.state = 191
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 192
                self.match(SplikitParser.T__5)
                pass
            elif token in [15]:
                self.state = 193
                self.match(SplikitParser.T__14)
                pass
            elif token in [34]:
                pass
            else:
                pass
            self.state = 196
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
            self.state = 198
            self.match(SplikitParser.T__15)
            self.state = 199
            self.expression()
            self.state = 200
            self.match(SplikitParser.T__4)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457688620) != 0):
                self.state = 201
                self.statement()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(SplikitParser.T__5)
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
            self.state = 209
            self.match(SplikitParser.Identifier)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 210
                self.match(SplikitParser.T__13)
                self.state = 211
                self.match(SplikitParser.Identifier)
                self.state = 216
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
            self.state = 217
            self.expression()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 218
                self.match(SplikitParser.T__13)
                self.state = 219
                self.expression()
                self.state = 224
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


        def Identifier(self):
            return self.getToken(SplikitParser.Identifier, 0)

        def argumentList(self):
            return self.getTypedRuleContext(SplikitParser.ArgumentListContext,0)


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
            self.state = 225
            self.primaryExpression()
            self.state = 226
            self.match(SplikitParser.T__16)
            self.state = 227
            self.match(SplikitParser.Identifier)
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 228
                self.match(SplikitParser.T__2)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457611304) != 0):
                    self.state = 229
                    self.argumentList()


                self.state = 232
                self.match(SplikitParser.T__3)


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
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.primaryExpression()
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 236
                        self.operator()
                        self.state = 237
                        self.expression() 
                    self.state = 243
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(SplikitParser.T__17)
                self.state = 245
                self.primaryExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
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
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(SplikitParser.T__2)
                self.state = 250
                self.expression()
                self.state = 251
                self.match(SplikitParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
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
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(SplikitParser.IntegerLiteral)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.match(SplikitParser.DecimalLiteral)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.match(SplikitParser.StringLiteral)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 4)
                self.state = 260
                self.match(SplikitParser.BooleanLiteral)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 261
                self.match(SplikitParser.NilLiteral)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 262
                self.match(SplikitParser.Identifier)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 7)
                self.state = 263
                self.match(SplikitParser.T__4)
                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 676457611304) != 0):
                    self.state = 264
                    self.argumentList()


                self.state = 267
                self.match(SplikitParser.T__5)
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
            self.state = 270
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





