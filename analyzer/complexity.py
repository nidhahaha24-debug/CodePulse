
import ast


class ComplexityVisitor(ast.NodeVisitor):

    def __init__(self):
        self.complexity = 1

    # Count if statements
    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    # Count for loops
    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    # Count while loops
    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    # Count exception handlers
    def visit_ExceptHandler(self, node):
        self.complexity += 1
        self.generic_visit(node)


def calculate_complexity(code):

    tree = ast.parse(code)

    results = []

    for node in ast.walk(tree):

        if isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef)
        ):

            visitor = ComplexityVisitor()

            visitor.visit(node)

            results.append({
                "function": node.name,
                "complexity": visitor.complexity,
                "line": node.lineno
            })

    return results


# Test complexity analyzer
if __name__ == "__main__":

    sample_code = """
def check_user(age, verified):

    if age >= 18:

        if verified:
            print("Allowed")

    for i in range(5):
        print(i)
"""

    results = calculate_complexity(sample_code)

    print("CodePulse Complexity Analysis")
    print("----------------------------")

    for result in results:

        print(
            f"Function: {result['function']} | "
            f"Complexity: {result['complexity']} | "
            f"Line: {result['line']}"
        )

