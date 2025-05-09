# Generated from TransportDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TransportDSLParser import TransportDSLParser
else:
    from TransportDSLParser import TransportDSLParser

# This class defines a complete listener for a parse tree produced by TransportDSLParser.
class TransportDSLListener(ParseTreeListener):

    # Enter a parse tree produced by TransportDSLParser#prog.
    def enterProg(self, ctx:TransportDSLParser.ProgContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#prog.
    def exitProg(self, ctx:TransportDSLParser.ProgContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#stat.
    def enterStat(self, ctx:TransportDSLParser.StatContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#stat.
    def exitStat(self, ctx:TransportDSLParser.StatContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#loadStmt.
    def enterLoadStmt(self, ctx:TransportDSLParser.LoadStmtContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#loadStmt.
    def exitLoadStmt(self, ctx:TransportDSLParser.LoadStmtContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#filterStmt.
    def enterFilterStmt(self, ctx:TransportDSLParser.FilterStmtContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#filterStmt.
    def exitFilterStmt(self, ctx:TransportDSLParser.FilterStmtContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#aggregateStmt.
    def enterAggregateStmt(self, ctx:TransportDSLParser.AggregateStmtContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#aggregateStmt.
    def exitAggregateStmt(self, ctx:TransportDSLParser.AggregateStmtContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#printStmt.
    def enterPrintStmt(self, ctx:TransportDSLParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#printStmt.
    def exitPrintStmt(self, ctx:TransportDSLParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#aggFunc.
    def enterAggFunc(self, ctx:TransportDSLParser.AggFuncContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#aggFunc.
    def exitAggFunc(self, ctx:TransportDSLParser.AggFuncContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#compOp.
    def enterCompOp(self, ctx:TransportDSLParser.CompOpContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#compOp.
    def exitCompOp(self, ctx:TransportDSLParser.CompOpContext):
        pass


    # Enter a parse tree produced by TransportDSLParser#value.
    def enterValue(self, ctx:TransportDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by TransportDSLParser#value.
    def exitValue(self, ctx:TransportDSLParser.ValueContext):
        pass



del TransportDSLParser