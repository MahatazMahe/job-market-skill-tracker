import sqlite3

import pandas as pd

from src.database import create_tables, save_postings, save_skills


def make_postings():
    return pd.DataFrame(
        {
            "job_id": [1, 2, 3],
            "company_name": ["Acme", "Beta", "Gamma"],
            "title": ["Data Engineer", "Cook", "Analyst"],
            "location": ["Dubai", "Austin", "Paris"],
            "description": ["Python and SQL", "We cook food", None],
            "is_repeat": [False, False, False],
            "is_relevant": [True, False, True],
        }
    )


def make_database():
    connection = sqlite3.connect(":memory:")
    create_tables(connection)
    save_postings(connection, make_postings())
    return connection


def test_save_skills_stores_one_row_per_skill():
    connection = make_database()
    save_skills(connection, make_postings())

    rows = connection.execute(
        "SELECT skill FROM posting_skills WHERE job_id = 1"
    ).fetchall()
    assert {row[0] for row in rows} == {"Python", "SQL"}


def test_save_skills_skips_postings_with_no_skills_or_no_description():
    connection = make_database()
    save_skills(connection, make_postings())

    count = connection.execute(
        "SELECT COUNT(*) FROM posting_skills WHERE job_id IN (2, 3)"
    ).fetchone()[0]
    assert count == 0


def test_save_skills_twice_does_not_duplicate():
    connection = make_database()
    save_skills(connection, make_postings())
    save_skills(connection, make_postings())

    count = connection.execute("SELECT COUNT(*) FROM posting_skills").fetchone()[0]
    assert count == 2