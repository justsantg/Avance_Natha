import os
from antlr4 import *
from TransportDSLLexer import TransportDSLLexer
from TransportDSLParser import TransportDSLParser
from interpreter import TransportVisitor

def ejecutar_script(path):
    print(f"\n--- Ejecutando {os.path.basename(path)} ---")
    input_stream = FileStream(path, encoding='utf-8')
    lexer = TransportDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TransportDSLParser(stream)
    tree = parser.prog()

    visitor = TransportVisitor()
    visitor.visit(tree)
    print(f"--- Fin de {os.path.basename(path)} ---\n")

if __name__ == "__main__":
    script_dir = "scripts"
    scripts = sorted([f for f in os.listdir(script_dir) if f.endswith(".dsl")])

    for script in scripts[:10]:  # Solo los primeros 10 scripts
        ejecutar_script(os.path.join(script_dir, script))
