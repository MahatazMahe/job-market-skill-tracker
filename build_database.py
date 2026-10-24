import sqlite3

from src.data_loader import get_data_directory
from src.database import create_tables, save_postings, save_skills
from src.ingest import load_postings
from src.quality import mark_repeats
from src.roles import is_relevant_title


def main():
    print("Loading postings...")
    postings = load_postings()
    postings = mark_repeats(postings)
    postings["is_relevant"] = postings["title"].apply(is_relevant_title)

    path = get_data_directory() / "processed" / "jobs.db"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()  # start clean so every run gives the same result

    connection = sqlite3.connect(path)
    create_tables(connection)

    print("Saving postings...")
    save_postings(connection, postings)

    print("Finding skills (this is the slow part)...")
    save_skills(connection, postings)

    posting_count = connection.execute("SELECT COUNT(*) FROM postings").fetchone()[0]
    skill_count = connection.execute("SELECT COUNT(*) FROM posting_skills").fetchone()[0]
    connection.close()

    print(f"Saved {posting_count} postings and {skill_count} posting-skill rows")
    print(f"Database: {path}")


if __name__ == "__main__":
    main()