import sqlite3

from src.data_loader import get_data_directory
from src.queries import skill_summary_from_db


def main():
    path = get_data_directory() / "processed" / "jobs.db"
    if not path.exists():
        print("Database not found. Build it first with: python build_database.py")
        return

    connection = sqlite3.connect(path)

    total, relevant, relevant_unique = connection.execute(
        """
        SELECT COUNT(*),
               SUM(is_relevant),
               SUM(is_relevant = 1 AND is_repeat = 0)
        FROM postings
        """
    ).fetchone()

    print("Source: Kaggle 'LinkedIn Job Postings (2023-2024)'. Mostly US, not UAE.")
    print(f"Database: {path}")
    print()
    print(f"All postings: {total}")
    print(f"Relevant to data/software roles: {relevant}")
    print(f"Relevant, repeats removed: {relevant_unique}")
    print()
    print(skill_summary_from_db(connection).to_string(index=False))

    connection.close()


if __name__ == "__main__":
    main()