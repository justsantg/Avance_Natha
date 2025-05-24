# Gestión de Transporte DSL

## Descripción

Este proyecto implementa un **Lenguaje Específico de Dominio (DSL)** para la gestión y análisis de datos de transporte de carga. Permite cargar datos desde un archivo CSV, aplicar filtros y agregaciones, y visualizar resultados de manera sencilla mediante scripts escritos en un lenguaje propio.

El sistema utiliza **ANTLR4** para el análisis léxico y sintáctico, y **Python** para la interpretación y ejecución de los scripts. Además, genera automáticamente el árbol de sintaxis de cada script usando **Graphviz**.

---

## Estructura del Proyecto

- **main.py**: Menú interactivo para seleccionar y ejecutar scripts DSL.
- **interpreter.py**: Implementa la lógica de interpretación y ejecución de los scripts.
- **TransportDSLLexer/TransportDSLParser**: Archivos generados por ANTLR4 para el análisis léxico y sintáctico.
- **scripts/**: Carpeta con ejemplos de scripts DSL listos para ejecutar.
- **arboles/**: Carpeta donde se generan los árboles de sintaxis en PDF de cada script ejecutado.
- **datos.csv**: Archivo de datos de transporte de ejemplo.
- **generar_csv.py**: Script para generar datos de ejemplo en formato CSV.

---

## ¿Cómo funciona?

### 1. Menú Interactivo

Al ejecutar `main.py`, se muestra un menú con los scripts disponibles. El usuario puede seleccionar el número de script que desea ejecutar.

### 2. Ejecución de un Script

Por cada script seleccionado:

- Se realiza un **análisis léxico** mostrando los tokens generados.
- Se realiza un **análisis sintáctico** y se genera el árbol de sintaxis en PDF (carpeta `arboles/`).
- Se ejecutan los filtros y agregaciones definidos en el script sobre el archivo `datos.csv`.
- Se muestran los resultados de las operaciones solicitadas (conteo, suma, promedio, etc.).

### 3. Ejemplo de Script DSL

```dsl
load "datos.csv";
filter column "estado_entrega" == "entregado";
aggregate count column "id_transporte";
print;
```

---

## Instalación y Requisitos

- **Python 3.8+**
- **ANTLR4** (para generar los analizadores léxico y sintáctico)
- **Graphviz** (para generar los árboles de sintaxis en PDF)
- **Librerías Python**:
  - pandas
  - antlr4-python3-runtime
  - faker (solo para generar datos de ejemplo)

Instala las dependencias con:

```bash
pip install pandas antlr4-python3-runtime faker
```

Instala Graphviz desde [https://graphviz.gitlab.io/download/](https://graphviz.gitlab.io/download/) y asegúrate de que el comando `dot` esté en tu PATH.

---

## Uso

1. **Genera datos de ejemplo** (opcional):

   ```bash
   python generar_csv.py
   ```

2. **Ejecuta el menú principal**:

   ```bash
   python main.py
   ```

3. **Selecciona un script** del menú para ver el análisis léxico, sintáctico y los resultados.

---

## Personalización

- Puedes crear tus propios scripts DSL en la carpeta `scripts/` siguiendo la sintaxis de los ejemplos.
- El archivo `datos.csv` puede ser reemplazado por tus propios datos, siempre que mantenga las columnas esperadas.

---

## Ejemplo de Salida