
import sys

from analyzer.analyzer import analyze_code
from analyzer.report import calculate_health_score, count_issues


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <python_file>")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' was not found.")
        return

    results = analyze_code(code)

    score = calculate_health_score(results)
    counts = count_issues(results)

    print("\nCodePulse Analysis")
    print("------------------")

    print(f"Health Score: {score}/100")

    print(f"High: {counts['High']}")
    print(f"Medium: {counts['Medium']}")
    print(f"Low: {counts['Low']}")

    print("\nIssues")
    print("------")

    if not results:
        print("No issues found.")
        return

    for issue in results:
        print(
            f"{issue['severity']}: "
            f"{issue['type']} - "
            f"Line {issue['line']} - "
            f"{issue['message']}"
        )


if __name__ == "__main__":
    main()

