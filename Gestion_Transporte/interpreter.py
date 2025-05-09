import pandas as pd
from TransportDSLParser import TransportDSLParser
from TransportDSLVisitor import TransportDSLVisitor

class TransportVisitor(TransportDSLVisitor):
    def __init__(self):
        self.data = None
        self.filters = []
        self.aggregations = []

    def visitLoadStmt(self, ctx):
        path = ctx.STRING().getText().strip('"')
        self.data = pd.read_csv(path)

    def visitFilterStmt(self, ctx):
        for i in range(0, len(ctx.STRING()), 1):
            col = ctx.STRING(i).getText().strip('"')
            op = ctx.compOp(i).getText()
            val = ctx.value(i).getText().strip('"')
            if val.replace('.', '', 1).isdigit():
                val = float(val) if '.' in val else int(val)
            self.filters.append((col, op, val))

    def visitAggregateStmt(self, ctx):
        func = ctx.aggFunc().getText()
        col = ctx.STRING().getText().strip('"')
        self.aggregations.append((func, col))

    def visitPrintStmt(self, ctx):
        df = self.data
        for col, op, val in self.filters:
            if op == '==': df = df[df[col] == val]
            elif op == '!=': df = df[df[col] != val]
            elif op == '>': df = df[df[col] > val]
            elif op == '<': df = df[df[col] < val]
            elif op == '>=': df = df[df[col] >= val]
            elif op == '<=': df = df[df[col] <= val]

        for func, col in self.aggregations:
            if func == 'count': print(f'count({col}) = {df[col].count()}')
            elif func == 'sum': print(f'sum({col}) = {df[col].sum()}')
            elif func == 'average': print(f'average({col}) = {df[col].mean()}')
