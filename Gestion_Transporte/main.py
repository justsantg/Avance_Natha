import os
from antlr4 import *
from TransportDSLLexer import TransportDSLLexer
from TransportDSLParser import TransportDSLParser
from interpreter import TransportVisitor

def mostrar_analisis_lexico(path):
    print("\n1️⃣ Análisis Léxico (Tokens generados):")
    input_stream = FileStream(path, encoding='utf-8')
    lexer = TransportDSLLexer(input_stream)
    tokens = []
    token = lexer.nextToken()
    while token.type != Token.EOF:
        tokens.append(f"[{lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] else token.text}]")
        token = lexer.nextToken()
    print(" ".join(tokens))
    print("")

def generar_arbol_graphviz(tree, parser, output_pdf):
    from antlr4.tree.Trees import Trees
    import tempfile
    def escape(s):
        return s.replace('"', '\\"')
    def to_dot(node, ruleNames, node_id=0, nodes=None, edges=None):
        if nodes is None: nodes = []
        if edges is None: edges = []
        label = escape(Trees.getNodeText(node, ruleNames))
        nodes.append(f'  node{node_id} [label="{label}"];')
        this_id = node_id
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = len(nodes)
            edges.append(f'  node{this_id} -> node{child_id};')
            to_dot(child, ruleNames, child_id, nodes, edges)
        return nodes, edges
    nodes, edges = to_dot(tree, parser.ruleNames)
    dot = "digraph G {\n" + "\n".join(nodes) + "\n" + "\n".join(edges) + "\n}"
    # Usar archivo temporal para .gv
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".gv") as tmpfile:
        tmpfile.write(dot)
        tmpfile_path = tmpfile.name
    # Generar solo el PDF
    try:
        import subprocess
        subprocess.run(["dot", "-Tpdf", tmpfile_path, "-o", output_pdf], check=True)
        print(f"Árbol de sintaxis generado: {output_pdf}")
    except Exception as e:
        print(f"No se pudo generar el PDF del árbol: {e}")
    finally:
        try:
            os.remove(tmpfile_path)
        except Exception:
            pass

def mostrar_analisis_sintactico(path, parser, tree):
    print("2️⃣ Análisis Sintáctico (Árbol de sintaxis):")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    arboles_dir = os.path.join(base_dir, "arboles")
    os.makedirs(arboles_dir, exist_ok=True)
    nombre = os.path.splitext(os.path.basename(path))[0]
    output_pdf = os.path.join(arboles_dir, f"arbol_{nombre}.pdf")
    generar_arbol_graphviz(tree, parser, output_pdf)
    print("")

def ejecutar_script(path):
    print(f"\n--- Ejecutando {os.path.basename(path)} ---")
    mostrar_analisis_lexico(path)
    input_stream = FileStream(path, encoding='utf-8')
    lexer = TransportDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TransportDSLParser(stream)
    tree = parser.prog()
    mostrar_analisis_sintactico(path, parser, tree)
    visitor = TransportVisitor()
    visitor.visit(tree)
    print(f"--- Fin de {os.path.basename(path)} ---\n")

if __name__ == "__main__":
    script_dir = "scripts"
    # Ordenar scripts por número
    def script_key(x):
        import re
        m = re.search(r'(\d+)', x)
        return int(m.group(1)) if m else 0
    scripts = sorted([f for f in os.listdir(script_dir) if f.endswith(".dsl")], key=script_key)
    scripts = scripts[:20]  # Solo los primeros 20 scripts

    while True:
        print("Menú de scripts disponibles:")
        for idx, script in enumerate(scripts, 1):
            print(f"{idx}. {script}")
        print("0. Salir")

        try:
            opcion = int(input("Digite el número del script a ejecutar (0 para salir): "))
        except ValueError:
            print("Por favor, ingrese un número válido.\n")
            continue

        if opcion == 0:
            print("Saliendo del programa.")
            break
        elif 1 <= opcion <= len(scripts):
            script_path = os.path.join(script_dir, scripts[opcion - 1])
            ejecutar_script(script_path)
        else:
            print("Opción no válida. Intente de nuevo.\n")
