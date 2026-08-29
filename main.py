
import sys

from analyzer.analyzer import analyze_code
from analyzer.report import calculate_health_score, count_issues
from analyzer.scanner import find_python_files


def analyze_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()

    except (FileNotFoundError, UnicodeDecodeError) as error:
        print(f"Error reading '{file_path}': {error}")
        return

    results = analyze_code(code)

    score = calculate_health_score(results)
    counts = count_issues(results)

    print("\n========================================")
    print("           CODEPULSE REPORT")
    print("========================================")

    print(f"\nFile: {file_path}")

    print("\nHealth Score")
    print("------------")
    print(f"{score}/100")

    print("\nSeverity Summary")
    print("----------------")
    print(f"High:     {counts['High']}")
    print(f"Medium:   {counts['Medium']}")
    print(f"Low:      {counts['Low']}")

    print("\nIssues")
    print("------")

    if not results:
        print("No issues found.")
        print("\n========================================")
        return

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

    print("========================================")


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <python_file_or_folder>")
        return

    path = sys.argv[1]

    python_files = find_python_files(path)

    if not python_files:
        print(f"No Python files found at '{path}'.")
        return

    print(f"\nFound {len(python_files)} Python file(s).")

    for file_path in python_files:
        analyze_file(file_path)


if __name__ == "__main__":
    main()
