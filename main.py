
import sys

from analyzer.analyzer import analyze_code


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

    print("\nCodePulse Analysis")
    print("------------------")

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
