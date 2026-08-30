
import json
import sys

from analyzer.analyzer import analyze_code
from analyzer.report import calculate_health_score, count_issues
from analyzer.scanner import find_python_files


def analyze_file(file_path, show_output=True):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()

    except (FileNotFoundError, UnicodeDecodeError) as error:
        if show_output:
            print(f"Error reading '{file_path}': {error}")
        return None

    results = analyze_code(code)

    score = calculate_health_score(results)
    counts = count_issues(results)

    if show_output:
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
        else:
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
        "file": str(file_path),
        "score": score,
        "counts": counts,
        "issues": results
    }


def create_project_summary(results):
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

    total_issues = total_high + total_medium + total_low

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

    return {
        "files_analyzed": total_files,
        "total_issues": total_issues,
        "severity_summary": {
            "high": total_high,
            "medium": total_medium,
            "low": total_low
        },
        "average_health_score": round(average_score, 1),
        "best_file": {
            "file": best_result["file"],
            "score": best_result["score"]
        },
        "needs_attention": {
            "file": worst_result["file"],
            "score": worst_result["score"]
        }
    }


def print_project_summary(summary):
    print("\n========================================")
    print("          PROJECT SUMMARY")
    print("========================================")

    print(f"\nFiles Analyzed: {summary['files_analyzed']}")
    print(f"Total Issues:   {summary['total_issues']}")

    print("\nSeverity Summary")
    print("----------------")
    print(f"High:     {summary['severity_summary']['high']}")
    print(f"Medium:   {summary['severity_summary']['medium']}")
    print(f"Low:      {summary['severity_summary']['low']}")

    print("\nAverage Health Score")
    print("--------------------")
    print(f"{summary['average_health_score']}/100")

    print("\nBest File")
    print("---------")
    print(
        f"{summary['best_file']['file']} "
        f"— {summary['best_file']['score']}/100"
    )

    print("\nNeeds Attention")
    print("---------------")
    print(
        f"{summary['needs_attention']['file']} "
        f"— {summary['needs_attention']['score']}/100"
    )

    print("\n========================================")


def main():
    arguments = sys.argv[1:]

    json_mode = "--json" in arguments
    arguments = [
        argument for argument in arguments
        if argument != "--json"
    ]

    if len(arguments) != 1:
        print("Usage: python main.py <python_file_or_folder> [--json]")
        return

    path = arguments[0]

    python_files = find_python_files(path)

    if not python_files:
        if json_mode:
            print(json.dumps({
                "error": f"No Python files found at '{path}'."
            }, indent=4))
        else:
            print(f"No Python files found at '{path}'.")
        return

    if not json_mode:
        print(f"\nFound {len(python_files)} Python file(s).")

    results = []

    for file_path in python_files:
        result = analyze_file(
            file_path,
            show_output=not json_mode
        )

        if result:
            results.append(result)

    if not results:
        return

    summary = create_project_summary(results)

    if json_mode:
        output = {
            "tool": "CodePulse",
            "files": results,
            "project_summary": summary
        }

        print(json.dumps(output, indent=4))

    else:
        print_project_summary(summary)


if __name__ == "__main__":
    main()
