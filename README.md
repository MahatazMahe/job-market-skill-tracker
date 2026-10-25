# Job Market Skill Tracker

This is my first real Python project. I'm learning data engineering, and I wanted something that works on real data instead of a tutorial. The idea is simple: take a pile of job postings, find which skills they mention, and count them.

I stopped at a working version on purpose, because I want to start the next project. What I didn't get to is listed at the end.

It runs on a Kaggle dataset that is mostly US jobs. I wanted UAE data, but I couldn't find enough of it (more on that below).

## What it does

Two scripts, one after the other:

1. `build_database.py` reads the postings from a CSV file. It marks the ones where a company posted the same text more than once, keeps the jobs whose title sounds like data, AI or software work, and looks for 10 skills in the descriptions (Python, SQL, AWS and so on). Everything goes into a SQLite database.
2. `main.py` reads that database and prints how many jobs mention each skill.

I checked the database by asking it the same question I had already answered with pandas. The counts matched exactly.

## Results

I loaded 123,849 postings. Only 4,031 had a title I counted as data, AI or software, and 3,615 were left after taking out repeats.

| Skill | Postings | Percent |
|---|---|---|
| Python | 1528 | 42.3 |
| SQL | 1352 | 37.4 |
| AWS | 1015 | 28.1 |
| Azure | 786 | 21.7 |
| Docker | 465 | 12.9 |
| Git | 459 | 12.7 |
| Spark | 319 | 8.8 |
| Power BI | 250 | 6.9 |
| Kafka | 227 | 6.3 |
| Airflow | 96 | 2.7 |

So Python shows up in about 4 out of 10 of these jobs. These numbers are only about this dataset. They don't tell you anything solid about the UAE.

## Data

I used the "LinkedIn Job Postings (2023 - 2024)" dataset by Arsh Koneru on Kaggle, which is CC BY-SA 4.0: https://www.kaggle.com/datasets/arshkon/linkedin-job-postings

The data isn't in this repo because the file is huge. To run the project, download `postings.csv` from Kaggle and put it in `data/raw/`.

## Running it

On Windows, in PowerShell:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python build_database.py
python main.py
```

`build_database.py` takes about a minute. It makes `data/processed/jobs.db` and deletes the old one first, so every run starts clean. The database isn't in the repo because anyone can rebuild it.

Tests run with `python -m pytest` (28 tests).

### Optional: the Jooble UAE sample

`collect_jooble.py` searches the Jooble API for UAE jobs and saves them to `data/raw/jooble_uae.json`. It needs a free API key in a file called `.env`:

```
JOOBLE_API_KEY=your-key-here
```

The script asks you to type `yes` before it sends anything, because the key has a request limit. The key and the collected file are not in the repo.

## Things that don't work well yet

- The Kaggle dataset has no UAE jobs. I searched for Dubai, Abu Dhabi, Sharjah and a few other spellings and got zero.
- I collected a small UAE sample from Jooble (81 unique jobs, 24 Oct 2026), but I didn't use it for skill percentages. The snippets are only 256 to 280 characters and centred on my search words, so I would mostly be counting my own searches. Three companies (Bybit, Mastercard and Binance) make up 83% of the jobs, and only 1 job showed a salary. `DECISIONS.md` has the details.
- Skills are found with simple text patterns, so some get missed. "PostgreSQL" doesn't count as SQL, for example.
- The job title filter only looks for certain words, so it will skip some relevant jobs.
- I used an AI assistant to help me learn and debug along the way.

## Where I stopped

Things I didn't build: more skills, a source of full UAE job descriptions, an API, a dashboard, Docker and automatic tests on GitHub. I'm moving on to the next project, where I'll learn FastAPI, Docker and CI.