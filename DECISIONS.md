# Decisions

## What this project is
I want to find out which skills employers ask for most in job postings, mainly in the UAE. The plan is to collect postings, pull the skills out of the text, store them, and count them.

## Why not Adzuna
I looked at Adzuna first because it has a proper API. But its country list doesn't include the UAE, so I dropped it.

## Why the Kaggle dataset
It's free and big: about 124,000 postings with the full job description. The problem is that I searched it for Dubai, Abu Dhabi, Sharjah and a few other spellings and found zero UAE jobs. It's mostly US data. So I'm using it to build and test my code, not to say anything about the UAE.

## What happened with Jooble
Jooble gave me a free key with a limit of 500 requests. My first test, "data engineer" in Dubai, returned nothing. Searching the whole country worked a little better, but not much: engineer gave 20 jobs, data 24, software engineer 7, machine learning 5, python 4 and AI 4. It also only gives a short snippet of each job, not the full text. So the UAE data I can get from it is small, and skills mentioned late in a long description might be missed.

## My plan
Build everything on the Kaggle data first, since it's big enough to test properly. Then run the same code on the small Jooble sample and show it as a UAE snapshot, saying clearly that it's small. I won't mix the two results together. I may try another UAE source later.

## Repeated postings
15,638 of 123,849 rows (about 12.6%) were the same company repeating the same description. I flag them instead of deleting them. Removing them changed the percentages by up to about 2.5 points but didn‘t change the top 4 skills.

## Which postings count as relevant
I count only postings whose title looks like a data, AI or software role. At first that gave 3,468. I found that it missed “Full Stack Engineer“ ,added a few words, and now get 4,031. It‘s approximate: it can still miss some roles.

## Jooble UAE sample: what I found and what I decided

I collected a UAE sample from the Jooble API on 24 Oct 2026. It used 12 searches
(page 1 only) and returned 81 unique jobs after removing repeats by Jooble's job id.

Before using it I checked the data, and three things stopped me from using it for
skill percentages:

1. The snippets are short. They are 256 to 280 characters and are excerpts around my search words, not full job descriptions. If I search "sql" and count snippets that mention SQL, I am mostly counting my own search.
2. The sample is dominated by a few employers. Bybit, Mastercard and Binance make up 67 of the 81 jobs (83%). Nearly all companies are in crypto, payments or fintech, so this is not a picture of the whole UAE market.
3. Salary is almost never shown. Only 1 of 81 jobs had one.

Decision: I do not report skill percentages or salaries for the UAE from this
sample. The skill results come from the Kaggle dataset, which is mostly US jobs.
The Jooble sample is kept only as a small, labelled snapshot of who was hiring in
the UAE on that day.

What would fix it: a source with full job descriptions for the UAE, and a
larger, more varied sample.