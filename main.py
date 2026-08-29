
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
        return None

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
        return {
            "score": score,
            "counts": counts,
            "issues": results
        }

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

    return {
        "score": score,
        "counts": counts,
        "issues": results
    }


def print_project_summary(results):
    total_files = len(results)

    total_high = sum(
        result["counts"]["High"]
        for result in results
    )

    total_medium = sum(
        result["counts"]["Medium"]
        for result in results
    )

    total_low = sum(
        result["counts"]["Low"]
        for result in results
    )

    average_score = sum(
        result["score"]
        for result in results
    ) / total_files

    best_result = max(
        results,
        key=lambda result: result["score"]
    )

    worst_result = min(
        results,
        key=lambda result: result["score"]
    )

    print("\n========================================")
    print("          PROJECT SUMMARY")
    print("========================================")

    print(f"\nFiles Analyzed: {total_files}")
    print(
        f"Total Issues:   "
        f"{total_high + total_medium + total_low}"
    )

    print("\nSeverity Summary")
    print("----------------")
    print(f"High:     {total_high}")
    print(f"Medium:   {total_medium}")
    print(f"Low:      {total_low}")

    print("\nAverage Health Score")
    print("--------------------")
    print(f"{average_score:.1f}/100")

    print("\nBest File")
    print("---------")
    print(
        f"{best_result['file']} "
        f"— {best_result['score']}/100"
    )

    print("\nNeeds Attention")
    print("---------------")
    print(
        f"{worst_result['file']} "
        f"— {worst_result['score']}/100"
    )

    print("\n========================================")


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

    results = []

    for file_path in python_files:
        result = analyze_file(file_path)

        if result:
            result["file"] = str(file_path)
            results.append(result)

    if results:
        print_project_summary(results)


if __name__ == "__main__":
    main()
