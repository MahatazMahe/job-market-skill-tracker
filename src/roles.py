import re

RELEVANT_TITLE_PATTERN = (
    r"data engineer|data analyst|data scientist|machine learning|"
    r"\bml\b|\bai\b|artificial intelligence|software engineer|"
    r"software developer|backend|back-end|analytics|"
    r"full stack|full-stack|fullstack|devops"
)


def is_relevant_title(title):
    """Return True if a job title looks like a data, AI or software role."""
    if not isinstance(title, str):
        return False
    return re.search(RELEVANT_TITLE_PATTERN, title, flags=re.IGNORECASE) is not None