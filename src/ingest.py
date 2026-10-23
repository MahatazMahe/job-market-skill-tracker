import pandas as pd

from src.data_loader import get_data_directory

REQUIRED_COLUMNS = ["job_id", "company_name", "title", "description", "location"]


def get_postings_path():
    """Return the path to the raw postings CSV file."""
    return get_data_directory() / "raw" / "postings.csv"


def load_postings(nrows=None):
    """Load the raw job postings, keeping only the columns we need.

    nrows: how many rows to read. None means read all of them.
    """
    csv_path = get_postings_path()

    if not csv_path.exists():
        raise FileNotFoundError(f"Postings file not found: {csv_path}")

    return pd.read_csv(csv_path, usecols=REQUIRED_COLUMNS, nrows=nrows)