import pandas as pd

from src.analytics import skill_summary


def test_counts_and_percentages():
    descriptions = pd.Series(["Python and SQL", "Python", "nothing"])

    table = skill_summary(descriptions)

    python_row = table[table["skill"] == "Python"].iloc[0]
    assert python_row["postings"] == 2
    assert python_row["percent"] == 66.7


def test_most_common_skill_comes_first():
    descriptions = pd.Series(["SQL", "SQL", "Python"])

    table = skill_summary(descriptions)

    assert table.iloc[0]["skill"] == "SQL"


def test_empty_input_gives_zero_percent():
    table = skill_summary(pd.Series([], dtype=str))

    assert (table["percent"] == 0.0).all()