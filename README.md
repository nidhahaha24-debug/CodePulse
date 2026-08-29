# CodePulse 🔍

**CodePulse** is a lightweight Python-based static code analysis tool that scans Python files and identifies common code-quality issues.

It uses Python's **AST (Abstract Syntax Tree)** to analyze source code without executing it.

## ✨ Features

* 🔎 Scan individual Python files or entire folders
* 🚫 Exclude test files from production analysis
* 🐛 Detect debug `print()` statements
* 🗑️ Detect unused variables
* ⚠️ Detect syntax errors
* 📊 Calculate cyclomatic complexity
* 🎯 Classify issues by severity
* 💯 Generate health scores
* 📋 Generate a project-wide summary
* 🧪 Automated tests using pytest

## 🛠️ Tech Stack

* **Python 3**
* **AST (Abstract Syntax Tree)**
* **Pytest**
* **Git & GitHub**

## 📁 Project Structure

```text
CodePulse/
│
├── analyzer/
│   ├── analyzer.py
│   ├── complexity.py
│   ├── report.py
│   └── scanner.py
│
├── tests/
│   └── test_analyzer.py
│
├── main.py
├── test_code.py
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd CodePulse
```

### 2. Install dependencies

```bash
pip install pytest
```

### 3. Run CodePulse

Analyze the entire project:

```bash
python main.py .
```

Or analyze a specific Python file:

```bash
python main.py test_code.py
```

## 📊 Example

CodePulse produces individual file reports:

```text
========================================
           CODEPULSE REPORT
========================================

File: main.py

Health Score
------------
100/100

Severity Summary
----------------
High:     0
Medium:   0
Low:      0

Issues
------
No issues found.
```

It also generates a project-wide summary showing:

* Total files analyzed
* Total issues
* High/Medium/Low issue counts
* Average health score
* Best-performing file
* File needing the most attention

## 🧪 Testing

Run the complete test suite:

```bash
python -m pytest
```

Expected result:

```text
5 passed
```

## 🎯 Severity Levels

| Severity | Complexity | Meaning                                 |
| -------- | ---------: | --------------------------------------- |
| Low      |        3–4 | Minor complexity/code-quality concern   |
| Medium   |        5–9 | Requires attention                      |
| High     |        10+ | Significant complexity or serious issue |

Complexity below 3 is considered acceptable.

## 💡 Why CodePulse?

Code quality problems are often discovered only after code becomes difficult to maintain.

CodePulse provides a simple way to identify common issues early and gives developers an easy-to-understand **health score** for their Python code.

## 🔮 Future Improvements

* HTML report generation
* JSON report export
* More AST-based code smells
* Duplicate-code detection
* Maintainability metrics
* Configurable analysis rules
* CI/CD integration
* GitHub Actions support
* Web-based dashboard

## 👩‍💻 Author

**Nidha Hussain**

Computer Science Engineering Student
Interested in Cloud Computing, Software Engineering, DevOps and AI.
