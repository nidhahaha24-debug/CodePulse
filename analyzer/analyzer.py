
import ast
from .complexity import calculate_complexity


def analyze_code(code):
    issues = []

    # Check for syntax errors
    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        issues.append({
            "type": "Syntax Error",
            "severity": "High",
            "line": error.lineno,
            "message": error.msg
        })
        return issues

    # Track assigned and used variables
    assigned_variables = {}
    used_variables = set()

    for node in ast.walk(tree):

        # Detect variables
        if isinstance(node, ast.Name):

            # Variable is assigned
            if isinstance(node.ctx, ast.Store):
                assigned_variables[node.id] = node.lineno

            # Variable is used
            elif isinstance(node.ctx, ast.Load):
                used_variables.add(node.id)

        # Detect print statements
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "print":
                issues.append({
                    "type": "Code Smell",
                    "severity": "Low",
                    "line": node.lineno,
                    "message": "Debug print statement found."
                })

    # Detect unused variables
    for variable, line in assigned_variables.items():

        if variable not in used_variables:
            issues.append({
                "type": "Code Smell",
                "severity": "Low",
                "line": line,
                "message": f"Variable '{variable}' is assigned but never used."
            })

    # Run complexity analysis
    complexity_results = calculate_complexity(code)

    for result in complexity_results:

        complexity = result["complexity"]

        if complexity >= 10:
            severity = "High"
        elif complexity >= 5:
            severity = "Medium"
        else:
            severity = "Low"

        issues.append({
            "type": "Complexity",
            "severity": severity,
            "line": result["line"],
            "message": (
                f"Function '{result['function']}' has "
                f"cyclomatic complexity of {complexity}."
            )
        })

    return issues


# Test CodePulse
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
