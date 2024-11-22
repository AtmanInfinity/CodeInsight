import ast
import sys

# Ensure that a script filename is provided
if len(sys.argv) != 2:
    print("Usage: python analyze_script.py <script_to_analyze.py>")
    sys.exit(1)

script_to_analyze = sys.argv[1]

try:
    with open(script_to_analyze, 'r') as file:
        node = ast.parse(file.read(), filename=script_to_analyze)
except FileNotFoundError:
    print(f"File '{script_to_analyze}' not found.")
    sys.exit(1)
except SyntaxError as e:
    print(f"Syntax error in '{script_to_analyze}': {e}")
    sys.exit(1)

for elem in ast.walk(node):
    if isinstance(elem, ast.FunctionDef):
        print(f"Function: {elem.name}")
    elif isinstance(elem, ast.ClassDef):
        print(f"Class: {elem.name}")
    elif isinstance(elem, ast.Import):
        for alias in elem.names:
            print(f"Import: {alias.name}")
    elif isinstance(elem, ast.ImportFrom):
        module = elem.module
        for alias in elem.names:
            print(f"From {module} import {alias.name}")
