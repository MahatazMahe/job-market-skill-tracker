import pandas as pd

COLUMNS = ["skill", "postings", "percent"]


def skill_summary_from_db(connection):
    """Count skills in relevant postings with repeats removed.

    Returns a DataFrame with the columns skill, postings and percent,
    sorted by postings (highest first), then by skill name.
    """
    total = connection.execute(
        "SELECT COUNT(*) FROM postings WHERE is_relevant = 1 AND is_repeat = 0"
    ).fetchone()[0]

    if total == 0:
        return pd.DataFrame(columns=COLUMNS)

    query = """
        SELECT skill,
               COUNT(*) AS postings,
               ROUND(100.0 * COUNT(*) / ?, 1) AS percent
        FROM posting_skills
        JOIN postings USING (job_id)
        WHERE postings.is_relevant = 1 AND postings.is_repeat = 0
        GROUP BY skill
        ORDER BY postings DESC, skill
    """
    rows = connection.execute(query, (total,)).fetchall()
    return pd.DataFrame(rows, columns=COLUMNS)