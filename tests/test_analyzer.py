
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

    for number in range(5):
        if number == value:
            return True

    return None
"""

    issues = analyze_code(code)

    complexity_issues = [
        issue
        for issue in issues
        if issue["type"] == "Complexity"
    ]

    assert len(complexity_issues) == 1
    assert complexity_issues[0]["severity"] == "Medium"
    assert "check_number" in complexity_issues[0]["message"]


def test_syntax_error_detection():
    code = """
def broken_function(
    print("Hello")
"""

    issues = analyze_code(code)

    assert len(issues) == 1
    assert issues[0]["type"] == "Syntax Error"
    assert issues[0]["severity"] == "High"


def test_health_score():
    from analyzer.report import calculate_health_score

    issues = [
        {"severity": "High"},
        {"severity": "Medium"},
        {"severity": "Low"},
    ]

    score = calculate_health_score(issues)

    assert score == 65
