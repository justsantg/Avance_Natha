# Generated from TransportDSL.g4 by ANTLR 4.13.2
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
        4,1,19,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,5,3,45,8,3,10,3,12,3,48,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,
        16,0,3,1,0,8,10,1,0,11,16,1,0,17,18,62,0,19,1,0,0,0,2,27,1,0,0,0,
        4,29,1,0,0,0,6,33,1,0,0,0,8,51,1,0,0,0,10,57,1,0,0,0,12,60,1,0,0,
        0,14,62,1,0,0,0,16,64,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,
        1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,28,3,4,2,0,24,
        28,3,6,3,0,25,28,3,8,4,0,26,28,3,10,5,0,27,23,1,0,0,0,27,24,1,0,
        0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,30,5,1,0,0,30,31,
        5,17,0,0,31,32,5,2,0,0,32,5,1,0,0,0,33,34,5,3,0,0,34,35,5,4,0,0,
        35,36,5,17,0,0,36,37,3,14,7,0,37,46,3,16,8,0,38,39,5,5,0,0,39,40,
        5,4,0,0,40,41,5,17,0,0,41,42,3,14,7,0,42,43,3,16,8,0,43,45,1,0,0,
        0,44,38,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,
        1,0,0,0,48,46,1,0,0,0,49,50,5,2,0,0,50,7,1,0,0,0,51,52,5,6,0,0,52,
        53,3,12,6,0,53,54,5,4,0,0,54,55,5,17,0,0,55,56,5,2,0,0,56,9,1,0,
        0,0,57,58,5,7,0,0,58,59,5,2,0,0,59,11,1,0,0,0,60,61,7,0,0,0,61,13,
        1,0,0,0,62,63,7,1,0,0,63,15,1,0,0,0,64,65,7,2,0,0,65,17,1,0,0,0,
        3,21,27,46
    ]

class TransportDSLParser ( Parser ):

    grammarFileName = "TransportDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'AND'", "'aggregate'", "'print'", "'count'", "'sum'", 
                     "'average'", "'>='", "'<='", "'>'", "'<'", "'=='", 
                     "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStmt = 2
    RULE_filterStmt = 3
    RULE_aggregateStmt = 4
    RULE_printStmt = 5
    RULE_aggFunc = 6
    RULE_compOp = 7
    RULE_value = 8

    ruleNames =  [ "prog", "stat", "loadStmt", "filterStmt", "aggregateStmt", 
                   "printStmt", "aggFunc", "compOp", "value" ]

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
    STRING=17
    NUMBER=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TransportDSLParser.StatContext)
            else:
                return self.getTypedRuleContext(TransportDSLParser.StatContext,i)


        def getRuleIndex(self):
            return TransportDSLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = TransportDSLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.stat()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 202) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStmt(self):
            return self.getTypedRuleContext(TransportDSLParser.LoadStmtContext,0)


        def filterStmt(self):
            return self.getTypedRuleContext(TransportDSLParser.FilterStmtContext,0)


        def aggregateStmt(self):
            return self.getTypedRuleContext(TransportDSLParser.AggregateStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(TransportDSLParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return TransportDSLParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = TransportDSLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.loadStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.filterStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.aggregateStmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.printStmt()
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


    class LoadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TransportDSLParser.STRING, 0)

        def getRuleIndex(self):
            return TransportDSLParser.RULE_loadStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStmt" ):
                listener.enterLoadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStmt" ):
                listener.exitLoadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStmt" ):
                return visitor.visitLoadStmt(self)
            else:
                return visitor.visitChildren(self)




    def loadStmt(self):

        localctx = TransportDSLParser.LoadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(TransportDSLParser.T__0)
            self.state = 30
            self.match(TransportDSLParser.STRING)
            self.state = 31
            self.match(TransportDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(TransportDSLParser.STRING)
            else:
                return self.getToken(TransportDSLParser.STRING, i)

        def compOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TransportDSLParser.CompOpContext)
            else:
                return self.getTypedRuleContext(TransportDSLParser.CompOpContext,i)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TransportDSLParser.ValueContext)
            else:
                return self.getTypedRuleContext(TransportDSLParser.ValueContext,i)


        def getRuleIndex(self):
            return TransportDSLParser.RULE_filterStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStmt" ):
                listener.enterFilterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStmt" ):
                listener.exitFilterStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStmt" ):
                return visitor.visitFilterStmt(self)
            else:
                return visitor.visitChildren(self)




    def filterStmt(self):

        localctx = TransportDSLParser.FilterStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(TransportDSLParser.T__2)
            self.state = 34
            self.match(TransportDSLParser.T__3)
            self.state = 35
            self.match(TransportDSLParser.STRING)
            self.state = 36
            self.compOp()
            self.state = 37
            self.value()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 38
                self.match(TransportDSLParser.T__4)
                self.state = 39
                self.match(TransportDSLParser.T__3)
                self.state = 40
                self.match(TransportDSLParser.STRING)
                self.state = 41
                self.compOp()
                self.state = 42
                self.value()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(TransportDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggFunc(self):
            return self.getTypedRuleContext(TransportDSLParser.AggFuncContext,0)


        def STRING(self):
            return self.getToken(TransportDSLParser.STRING, 0)

        def getRuleIndex(self):
            return TransportDSLParser.RULE_aggregateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStmt" ):
                listener.enterAggregateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStmt" ):
                listener.exitAggregateStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStmt" ):
                return visitor.visitAggregateStmt(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStmt(self):

        localctx = TransportDSLParser.AggregateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregateStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(TransportDSLParser.T__5)
            self.state = 52
            self.aggFunc()
            self.state = 53
            self.match(TransportDSLParser.T__3)
            self.state = 54
            self.match(TransportDSLParser.STRING)
            self.state = 55
            self.match(TransportDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TransportDSLParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = TransportDSLParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(TransportDSLParser.T__6)
            self.state = 58
            self.match(TransportDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TransportDSLParser.RULE_aggFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggFunc" ):
                listener.enterAggFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggFunc" ):
                listener.exitAggFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggFunc" ):
                return visitor.visitAggFunc(self)
            else:
                return visitor.visitChildren(self)




    def aggFunc(self):

        localctx = TransportDSLParser.AggFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aggFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
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


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TransportDSLParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = TransportDSLParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(TransportDSLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(TransportDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return TransportDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = TransportDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
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





