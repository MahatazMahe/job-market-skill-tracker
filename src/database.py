import pandas as pd

from src.skills import extract_skills


def create_tables(connection):
    """Create the two tables if they do not exist yet.

    postings        one row per job posting
    posting_skills  one row per skill found in a posting
    """
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS postings (
            job_id        INTEGER PRIMARY KEY,
            company_name  TEXT,
            title         TEXT,
            location      TEXT,
            description   TEXT,
            is_repeat     INTEGER NOT NULL,
            is_relevant   INTEGER NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS posting_skills (
            job_id  INTEGER NOT NULL,
            skill   TEXT NOT NULL,
            PRIMARY KEY (job_id, skill),
            FOREIGN KEY (job_id) REFERENCES postings (job_id)
        )
        """
    )
    connection.commit()


def _to_sql_value(value):
    """Turn a missing value (NaN or None) into None, which SQLite stores as NULL."""
    if pd.isna(value):
        return None
    return value


def save_postings(connection, postings):
    """Write postings into the postings table.

    `postings` is a DataFrame with the columns job_id, company_name, title,
    location, description, is_repeat and is_relevant. If a job_id is already
    in the table, its row is replaced, so running this twice is safe.
    """
    rows = [
        (
            int(row.job_id),
            _to_sql_value(row.company_name),
            _to_sql_value(row.title),
            _to_sql_value(row.location),
            _to_sql_value(row.description),
            int(row.is_repeat),
            int(row.is_relevant),
        )
        for row in postings.itertuples(index=False)
    ]

    connection.executemany(
        """
        INSERT OR REPLACE INTO postings
            (job_id, company_name, title, location, description,
             is_repeat, is_relevant)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )
    connection.commit()


def save_skills(connection, postings):
    """Find the skills in each description and store one row per skill.

    Postings with no description are skipped. A skill already stored for a
    posting is ignored, so running this twice is safe.
    """
    rows = []
    for row in postings.itertuples(index=False):
        if not isinstance(row.description, str):
            continue
        for skill in extract_skills(row.description):
            rows.append((int(row.job_id), skill))

    connection.executemany(
        "INSERT OR IGNORE INTO posting_skills (job_id, skill) VALUES (?, ?)",
        rows,
    )
    connection.commit()