# CodePulse 🔍

**CodePulse** is a Python-based static code analysis tool that automatically examines source code to identify potential code-quality issues, syntax errors, and complex functions.

The project is designed to help developers detect common problems early and understand the maintainability of their code.

## 🚀 Features

* 🔴 **Syntax Error Detection**

  * Identifies invalid Python syntax without crashing the analyzer.

* 🟡 **Code Smell Detection**

  * Detects debug `print()` statements.
  * Identifies variables that are assigned but never used.

* 📊 **Cyclomatic Complexity Analysis**

  * Calculates the complexity of individual functions.
  * Flags functions with higher complexity.

* 🧩 **AST-Based Analysis**

  * Uses Python's Abstract Syntax Tree (AST) to analyze code structure rather than relying only on text matching.

## 🏗️ Project Structure

```text
CodePulse/
│
├── analyzer/
│   ├── analyzer.py
│   └── complexity.py
│
├── main.py
├── .gitignore
└── README.md
```

## ⚙️ How It Works

```text
Python Source Code
        │
        ▼
   AST Parser
        │
        ▼
┌───────────────────────┐
│   CodePulse Analyzer  │
├───────────────────────┤
│ Syntax Analysis       │
│ Code Smell Detection  │
│ Complexity Analysis   │
└───────────┬───────────┘
            │
            ▼
      Analysis Report
```

## 🛠️ Technologies

* Python 3
* Python AST
* Git
* GitHub
* Visual Studio Code

## ▶️ Running the Project

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project:

```bash
cd CodePulse
```

Run the analyzer:

```bash
python analyzer/analyzer.py
```

## 📌 Example

Given code containing nested conditions and debug statements, CodePulse can produce output such as:

```text
CodePulse Analysis
------------------
Low: Code Smell - Line 16 - Debug print statement found.
Low: Code Smell - Line 10 - Debug print statement found.
Low: Code Smell - Line 7 - Debug print statement found.
Low: Complexity - Line 2 - Function 'check_user' has cyclomatic complexity of 4.
```

## 🔮 Future Improvements

The project is planned to evolve into a more complete developer-focused code analysis platform.

Planned improvements include:

* Security vulnerability detection
* More advanced code-quality rules
* Function-level metrics
* Maintainability scoring
* Automated test generation
* REST API for code analysis
* Web-based dashboard
* GitHub repository integration
* Automated analysis through CI/CD pipelines

## 🎯 Project Goal

The long-term goal of CodePulse is to provide developers with an accessible automated code-review assistant that can analyze code, identify potential problems, and provide actionable recommendations.

---

**Built with Python 🐍**
