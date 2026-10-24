import json
import os
from datetime import datetime, timezone

from dotenv import load_dotenv

from src.data_loader import get_data_directory
from src.jooble import collect_jobs

KEYWORDS = [
    "data engineer",
    "data analyst",
    "data scientist",
    "machine learning",
    "AI engineer",
    "software engineer",
    "python",
    "sql",
    "data",
    "analytics",
    "cloud",
    "devops",
]


def main():
    load_dotenv()
    api_key = os.getenv("JOOBLE_API_KEY")
    if not api_key:
        print("JOOBLE_API_KEY was not found. Check your .env file.")
        return

    print(f"This will use {len(KEYWORDS)} of your 500 Jooble requests.")
    if input("Type yes to continue: ").strip().lower() != "yes":
        print("Cancelled. No requests were sent.")
        return

    jobs = collect_jobs(api_key, KEYWORDS)

    output = {
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "source": "Jooble API, location: United Arab Emirates, page 1 only",
        "jobs": jobs,
    }
    path = get_data_directory() / "raw" / "jooble_uae.json"
    path.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(f"Saved {len(jobs)} unique jobs to {path}")


if __name__ == "__main__":
    main()