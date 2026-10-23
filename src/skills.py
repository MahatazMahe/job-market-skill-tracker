import re

# Each skill has a name and a pattern that finds it in text.
# \b means "word boundary", so the pattern for sql will not match inside "mysql".
SKILL_PATTERNS = {
    "Python": r"\bpython\b",
    "SQL": r"\bsql\b",
    "AWS": r"\baws\b|\bamazon web services\b",
    "Azure": r"\bazure\b",
    "Docker": r"\bdocker\b",
    "Spark": r"\bspark\b",
    "Kafka": r"\bkafka\b",
    "Airflow": r"\bairflow\b",
    "Git": r"\bgit\b",
    "Power BI": r"\bpower\s?bi\b",
}


def extract_skills(text):
    """Return the set of skill names found in a piece of text."""
    if not isinstance(text, str):
        return set()

    found = set()
    for skill, pattern in SKILL_PATTERNS.items():
        if re.search(pattern, text, flags=re.IGNORECASE):
            found.add(skill)
    return found