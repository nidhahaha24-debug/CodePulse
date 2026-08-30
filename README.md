
# CodePulse 🔍

**CodePulse** is a lightweight Python-based static code analysis tool that scans Python source code and identifies common code-quality issues.

It uses Python's **AST (Abstract Syntax Tree)** to analyze source code without executing it, helping developers identify potential problems early and understand the overall health of their code.

## ✨ Features

* 🔎 Scan individual Python files or entire folders
* 🚫 Exclude test files and CodePulse's internal files during project scanning
* 🐛 Detect debug `print()` statements
* 🗑️ Detect unused variables
* ⚠️ Detect syntax errors
* 📊 Calculate cyclomatic complexity
* 🎯 Classify issues by severity
* 💯 Calculate code health scores
* 📋 Generate project-wide summaries
* 📦 Export analysis results as JSON
* 🧪 Automated testing with pytest

## 🛠️ Tech Stack

* **Python 3**
* **AST (Abstract Syntax Tree)**
* **Pytest**
* **Git & GitHub**

## 📸 Screenshots

### CLI Analysis

![CodePulse CLI Analysis](screenshots/cli-analysis.png)

### JSON Output

![CodePulse JSON Output](screenshots/json-output.png)

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
├── screenshots/
│   ├── cli-analysis.png
│   └── json-output.png
│
├── main.py
├── test_code.py
├── requirements.txt
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
pip install -r requirements.txt
```

### 3. Run CodePulse

Analyze an entire project:

```bash
python main.py .
```

Analyze a specific Python file:

```bash
python main.py test_code.py
```

Generate JSON output:

```bash
python main.py . --json
```

## 📊 Example Output

```text
========================================
           CODEPULSE REPORT
========================================

File: test_code.py

Health Score
------------
70/100

Severity Summary
----------------
High:     0
Medium:   1
Low:      1

Issues
------
Medium: Complexity - Function 'example'
has cyclomatic complexity of 6.

Recommendation:
Consider breaking this function into smaller functions.
```

For project analysis, CodePulse also provides:

* Total files analyzed
* Total issues
* Severity summary
* Average health score
* Best-performing file
* File needing the most attention

## 📦 JSON Output

CodePulse supports machine-readable JSON output:

```bash
python main.py . --json
```

The JSON report contains individual file results, health scores, issue details, severity counts, and a project-wide summary.

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

| Severity | Complexity | Meaning                                  |
| -------- | ---------: | ---------------------------------------- |
| Low      |        3–4 | Minor complexity or code-quality concern |
| Medium   |        5–9 | Requires attention                       |
| High     |        10+ | Significant complexity or serious issue  |

Complexity below 5 is considered acceptable.

## 💡 Why CodePulse?

Code-quality problems are often discovered only after code becomes difficult to maintain.

CodePulse provides a simple way to identify common issues early and gives developers an easy-to-understand **health score** for their Python code.

The goal is to make static analysis simple, lightweight, and accessible without executing the analyzed code.

## 🔮 Future Improvements

* HTML report generation
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

Interested in Cloud Computing, Software Engineering, DevOps, and AI.
