import pandas as pd

from src.skills import count_skills


def skill_summary(descriptions):
    """Return a table of skills with posting counts and percentages.

    descriptions: a pandas Series of job description texts.
    The percentage is out of all the descriptions given.
    """
    total = len(descriptions)
    counts = count_skills(descriptions)

    table = pd.DataFrame(
        {"skill": list(counts.keys()), "postings": list(counts.values())}
    )

    if total == 0:
        table["percent"] = 0.0
    else:
        table["percent"] = (100 * table["postings"] / total).round(1)

    return table.sort_values("postings", ascending=False, kind="stable").reset_index(drop=True)