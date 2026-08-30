
import ast

from .complexity import calculate_complexity


def is_main_block(node):
    """Check whether an AST If node is an if __name__ == '__main__' block."""
    return (
        isinstance(node, ast.If)
        and isinstance(node.test, ast.Compare)
        and isinstance(node.test.left, ast.Name)
        and node.test.left.id == "__name__"
        and len(node.test.ops) == 1
        and isinstance(node.test.ops[0], ast.Eq)
        and len(node.test.comparators) == 1
        and isinstance(node.test.comparators[0], ast.Constant)
        and node.test.comparators[0].value == "__main__"
    )


def get_main_block_lines(tree):
    """Return line numbers inside the main execution block."""
    main_lines = set()

    for node in ast.walk(tree):
        if is_main_block(node):
            for child in ast.walk(node):
                if hasattr(child, "lineno"):
                    main_lines.add(child.lineno)

    return main_lines


def get_output_function_lines(tree):
    """Return line numbers belonging to intentional output functions."""
    output_lines = set()

    output_functions = {
        "main",
        "analyze_file",
        "print_project_summary",
        "create_project_summary",
    }

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in output_functions:
                for child in ast.walk(node):
                    if hasattr(child, "lineno"):
                        output_lines.add(child.lineno)

    return output_lines


def analyze_print_statements(tree, ignored_lines):
    """Find print statements that are likely to be debug statements."""
    issues = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        if not isinstance(node.func, ast.Name):
            continue

        if node.func.id != "print":
            continue

        if node.lineno in ignored_lines:
            continue

        issues.append({
            "type": "Code Smell",
            "severity": "Low",
            "line": node.lineno,
            "message": "Debug print statement found.",
            "recommendation": (
                "Remove debug print statements before production."
            )
        })

    return issues


def analyze_variables(tree):
    """Find variables that are assigned but never used."""
    issues = []

    assigned_variables = {}
    used_variables = set()

    for node in ast.walk(tree):
        if not isinstance(node, ast.Name):
            continue

        if isinstance(node.ctx, ast.Store):
            assigned_variables[node.id] = node.lineno

        elif isinstance(node.ctx, ast.Load):
            used_variables.add(node.id)

    for variable, line in assigned_variables.items():
        if variable not in used_variables:
            issues.append({
                "type": "Code Smell",
                "severity": "Low",
                "line": line,
                "message": (
                    f"Variable '{variable}' is assigned but never used."
                ),
                "recommendation": (
                    "Remove the unused variable if it is not required."
                )
            })

    return issues


def analyze_complexity(code):
    """Analyze function complexity."""
    issues = []

    complexity_results = calculate_complexity(code)

    for result in complexity_results:
        complexity = result["complexity"]

        # Complexity below 5 is considered acceptable.
        if complexity < 5:
            continue

        if complexity >= 10:
            severity = "High"
        else:
            severity = "Medium"

        issues.append({
            "type": "Complexity",
            "severity": severity,
            "line": result["line"],
            "message": (
                f"Function '{result['function']}' has "
                f"cyclomatic complexity of {complexity}."
            ),
            "recommendation": (
                "Consider breaking this function into smaller functions."
            )
        })

    return issues


def analyze_code(code):
    """Analyze Python code and return detected issues."""
    issues = []

    # Check for syntax errors.
    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        issues.append({
            "type": "Syntax Error",
            "severity": "High",
            "line": error.lineno,
            "message": error.msg,
            "recommendation": (
                "Fix the syntax error before running the program."
            )
        })
        return issues

    # Identify lines where print statements are intentional.
    main_block_lines = get_main_block_lines(tree)
    output_function_lines = get_output_function_lines(tree)

    ignored_print_lines = (
        main_block_lines | output_function_lines
    )

    # Detect debug print statements.
    issues.extend(
        analyze_print_statements(
            tree,
            ignored_print_lines
        )
    )

    # Detect unused variables.
    issues.extend(
        analyze_variables(tree)
    )

    # Detect complexity.
    issues.extend(
        analyze_complexity(code)
    )

    return issues


if __name__ == "__main__":

    sample_code = """
def check_user(age, verified):

    if age >= 18:

        if verified:
            print("Allowed")

    for i in range(5):
        print(i)


name = "Nidha"
age = 21

print(name)
"""

    results = analyze_code(sample_code)

    print("CodePulse Analysis")
    print("------------------")

    for issue in results:
        print(
            f"{issue['severity']}: "
            f"{issue['type']} - "
            f"Line {issue['line']} - "
            f"{issue['message']}"
        )

        print(
            f"Recommendation: "
            f"{issue['recommendation']}"
        )

        print()
