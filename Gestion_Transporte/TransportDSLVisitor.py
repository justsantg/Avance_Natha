# Generated from TransportDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TransportDSLParser import TransportDSLParser
else:
    from TransportDSLParser import TransportDSLParser

# This class defines a complete generic visitor for a parse tree produced by TransportDSLParser.

class TransportDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TransportDSLParser#prog.
    def visitProg(self, ctx:TransportDSLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#stat.
    def visitStat(self, ctx:TransportDSLParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#loadStmt.
    def visitLoadStmt(self, ctx:TransportDSLParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#filterStmt.
    def visitFilterStmt(self, ctx:TransportDSLParser.FilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#aggregateStmt.
    def visitAggregateStmt(self, ctx:TransportDSLParser.AggregateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#printStmt.
    def visitPrintStmt(self, ctx:TransportDSLParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#aggFunc.
    def visitAggFunc(self, ctx:TransportDSLParser.AggFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#compOp.
    def visitCompOp(self, ctx:TransportDSLParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TransportDSLParser#value.
    def visitValue(self, ctx:TransportDSLParser.ValueContext):
        return self.visitChildren(ctx)



del TransportDSLParser