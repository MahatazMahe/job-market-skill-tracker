# Job Market Skill Tracker

This is my first real Python project. I'm learning data engineering, and I wanted something that works on real data instead of a tutorial. The idea is simple: take a pile of job postings, find which skills they mention, and count them.

It's not finished. Right now it runs on a Kaggle dataset that is mostly US jobs. I wanted UAE data, but I couldn't find enough of it yet (more on that below).

## What it does

It reads the postings from a CSV file and marks the ones where a company posted the same text more than once. Then it keeps the jobs whose title sounds like data, AI or software work, and looks for 10 skills in the descriptions (Python, SQL, AWS and so on). At the end it prints how many jobs mention each skill.

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
python main.py
```

Tests run with `pytest`.

## Things that don't work well yet

- The dataset has no UAE jobs. I searched for Dubai, Abu Dhabi, Sharjah and a few other spellings and got zero.
- Skills are found with simple text patterns, so some get missed. "PostgreSQL" doesn't count as SQL, for example.
- The job title filter only looks for certain words, so it will skip some relevant jobs.
- I tried the Jooble API for UAE jobs. It only gave me a few dozen per keyword, and only a short snippet of each, which isn't enough for real conclusions.
- I used an AI assistant to help me learn and debug along the way.

## What's next

Try the same code on the small UAE sample (and say clearly that it's small), store the results in SQLite, and add more skills and tests.