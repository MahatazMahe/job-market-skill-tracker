import sqlite3

import pandas as pd

from src.database import create_tables, save_postings


def make_postings():
    return pd.DataFrame(
        {
            "job_id": [1, 2],
            "company_name": ["Acme", "Beta"],
            "title": ["Data Engineer", "Cook"],
            "location": ["Dubai", "Austin"],
            "description": ["Python and SQL", None],
            "is_repeat": [False, True],
            "is_relevant": [True, False],
        }
    )


def make_database():
    connection = sqlite3.connect(":memory:")
    create_tables(connection)
    return connection


def test_create_tables_makes_both_tables():
    connection = make_database()

    rows = connection.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table'"
    ).fetchall()
    names = {row[0] for row in rows}

    assert names == {"postings", "posting_skills"}


def test_create_tables_can_run_twice():
    connection = make_database()
    create_tables(connection)  # should not raise an error


def test_save_postings_stores_every_row():
    connection = make_database()
    save_postings(connection, make_postings())

    count = connection.execute("SELECT COUNT(*) FROM postings").fetchone()[0]
    assert count == 2


def test_save_postings_keeps_missing_description_as_null():
    connection = make_database()
    save_postings(connection, make_postings())

    description = connection.execute(
        "SELECT description FROM postings WHERE job_id = 2"
    ).fetchone()[0]
    assert description is None


def test_save_postings_twice_does_not_duplicate():
    connection = make_database()
    save_postings(connection, make_postings())
    save_postings(connection, make_postings())

    count = connection.execute("SELECT COUNT(*) FROM postings").fetchone()[0]
    assert count == 2