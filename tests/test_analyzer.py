from analyzer.analyzer import analyze_code


def test_debug_print_detection():
    code = """
print("Hello")
"""

    issues = analyze_code(code)

    assert len(issues) == 1
    assert issues[0]["type"] == "Code Smell"
    assert issues[0]["severity"] == "Low"


def test_unused_variable_detection():
    code = """
def test_function():
    unused_value = 10
    return 5
"""

    issues = analyze_code(code)

    assert any(
        issue["type"] == "Code Smell"
        and "unused" in issue["message"].lower()
        for issue in issues
    )


def test_complexity_detection():
    code = """
def check_number(value):
    if value > 10:
        return True

    if value < 0:
        return False

    return None
"""

    issues = analyze_code(code)

    complexity_issues = [
        issue
        for issue in issues
        if issue["type"] == "Complexity"
    ]

    assert len(complexity_issues) == 1
    assert "check_number" in complexity_issues[0]["message"]
    