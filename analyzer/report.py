def calculate_health_score(issues):
    score = 100

    for issue in issues:
        severity = issue["severity"]

        if severity == "High":
            score -= 20

        elif severity == "Medium":
            score -= 10

        elif severity == "Low":
            score -= 5

    return max(score, 0)


def count_issues(issues):
    counts = {
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for issue in issues:
        severity = issue["severity"]

        if severity in counts:
            counts[severity] += 1

    return counts
if __name__ == "__main__":

    test_issues = [
        {
            "severity": "High"
        },
        {
            "severity": "Medium"
        },
        {
            "severity": "Low"
        },
        {
            "severity": "Low"
        }
    ]

    score = calculate_health_score(test_issues)
    counts = count_issues(test_issues)

    print("CodePulse Health Score")
    print("----------------------")
    print(f"Score: {score}/100")
    print(f"High: {counts['High']}")
    print(f"Medium: {counts['Medium']}")
    print(f"Low: {counts['Low']}")