
from pathlib import Path


EXCLUDED_DIRECTORIES = {
    ".git",
    "__pycache__",
    "tests",
}

EXCLUDED_FILES = {
    "main.py",
    "analyzer.py",
    "complexity.py",
    "report.py",
    "scanner.py",
}


def find_python_files(path):
    target = Path(path)

    if target.is_file():
        if target.suffix == ".py":
            return [target]
        return []

    if target.is_dir():
        python_files = []

        for file in target.rglob("*.py"):
            if any(
                excluded in file.parts
                for excluded in EXCLUDED_DIRECTORIES
            ):
                continue

            if file.name in EXCLUDED_FILES:
                continue

            python_files.append(file)

        return python_files

    return []
