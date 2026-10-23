def profile_postings(postings):
    """Return simple data-quality counts for a table of job postings."""
    total_rows = len(postings)

    return {
        "total_rows": total_rows,
        "missing_title": int(postings["title"].isna().sum()),
        "missing_description": int(postings["description"].isna().sum()),
        "missing_location": int(postings["location"].isna().sum()),
        "duplicate_job_ids": int(postings["job_id"].duplicated().sum()),
        "duplicate_descriptions": int(postings["description"].duplicated().sum()),
    }


def mark_repeats(postings):
    """Return a copy of the postings with an is_repeat column.

    A row is a repeat when the same company already posted the same
    description earlier in the table. Nothing is deleted.
    """
    marked = postings.copy()
    marked["is_repeat"] = marked.duplicated(subset=["company_name", "description"])
    return marked