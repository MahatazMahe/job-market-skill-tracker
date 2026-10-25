import sqlite3

import pandas as pd

from src.database import create_tables, save_postings, save_skills
from src.queries import skill_summary_from_db


def make_database(rows):
    postings = pd.DataFrame(
        rows,
        columns=[
            "job_id", "company_name", "title", "location",
            "description", "is_repeat", "is_relevant",
        ],
    )
    connection = sqlite3.connect(":memory:")
    create_tables(connection)
    save_postings(connection, postings)
    save_skills(connection, postings)
    return connection


def test_counts_and_percentages():
    connection = make_database(
        [
            (1, "A", "Data Engineer", "Dubai", "Python and SQL", False, True),
            (2, "B", "Data Analyst", "Dubai", "Python", False, True),
        ]
    )

    result = skill_summary_from_db(connection)

    assert result.to_dict("records") == [
        {"skill": "Python", "postings": 2, "percent": 100.0},
        {"skill": "SQL", "postings": 1, "percent": 50.0},
    ]


def test_ignores_repeats_and_irrelevant_postings():
    connection = make_database(
        [
            (1, "A", "Data Engineer", "Dubai", "Python and SQL", False, True),
            (2, "B", "Data Engineer", "Dubai", "Python Docker", True, True),
            (3, "C", "Cook", "Dubai", "Python", False, False),
        ]
    )

    result = skill_summary_from_db(connection)

    assert list(result["skill"]) == ["Python", "SQL"]
    assert list(result["postings"]) == [1, 1]


def test_returns_empty_table_when_nothing_is_relevant():
    connection = make_database(
        [(1, "A", "Cook", "Dubai", "Python", False, False)]
    )

    result = skill_summary_from_db(connection)

    assert result.empty
    assert list(result.columns) == ["skill", "postings", "percent"]