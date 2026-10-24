import html
import re

import requests


def clean_snippet(text):
    """Turn a Jooble snippet into plain text.

    Removes HTML tags like <b>, converts codes like &nbsp; into normal
    characters, and collapses extra spaces and line breaks.
    """
    if not isinstance(text, str):
        return ""

    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def search_jooble(api_key, keywords, location="United Arab Emirates", page=1):
    """Send one search to Jooble. Returns the list of jobs, or None on failure."""
    url = f"https://jooble.org/api/{api_key}"
    body = {"keywords": keywords, "location": location, "page": page}

    try:
        response = requests.post(url, json=body, timeout=30)
    except requests.RequestException as error:
        print(f"Network problem: {type(error).__name__}")
        return None

    if response.status_code != 200:
        print(f"Request failed with status {response.status_code}")
        return None

    return response.json().get("jobs", [])


def collect_jobs(api_key, keyword_list):
    """Run one search per keyword and return the jobs without duplicates.

    Each job gets a "searched_keyword" field. A job found by several
    keywords is kept once, using Jooble's id.
    """
    jobs_by_id = {}

    for keyword in keyword_list:
        jobs = search_jooble(api_key, keyword)
        if jobs is None:
            continue
        print(f"{keyword}: {len(jobs)} jobs")
        for job in jobs:
            job_id = job.get("id")
            if job_id not in jobs_by_id:
                job["searched_keyword"] = keyword
                jobs_by_id[job_id] = job

    return list(jobs_by_id.values())