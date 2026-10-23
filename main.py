from src.analytics import skill_summary
from src.data_loader import get_data_directory, get_project_root
from src.ingest import load_postings
from src.quality import mark_repeats
from src.roles import is_relevant_title


def main():
    print("Job Market Skill Tracker")
    print(f"Project root: {get_project_root()}")
    print(f"Data directory: {get_data_directory()}")
    print()

    postings = mark_repeats(load_postings())
    relevant = postings[postings["title"].apply(is_relevant_title)]
    unique_relevant = relevant[~relevant["is_repeat"]]

    print("Source: Kaggle 'LinkedIn Job Postings (2023-2024)'. Mostly US, not UAE.")
    print(f"All postings: {len(postings)}")
    print(f"Relevant postings (data, AI or software titles): {len(relevant)}")
    print(f"Relevant postings with repeats removed: {len(unique_relevant)}")
    print()

    print("Skill demand, repeats removed:")
    print(skill_summary(unique_relevant["description"]).to_string(index=False))


if __name__ == "__main__":
    main()