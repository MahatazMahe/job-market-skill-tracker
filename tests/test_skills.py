from src.skills import extract_skills


def test_finds_a_skill_in_plain_text():
    assert extract_skills("We need Python experience") == {"Python"}


def test_ignores_upper_and_lower_case():
    assert extract_skills("PYTHON and sql") == {"Python", "SQL"}


def test_does_not_match_inside_other_words():
    assert extract_skills("We use MySQL and GitHub") == set()


def test_counts_a_skill_only_once():
    assert extract_skills("Python, python, PYTHON") == {"Python"}


def test_missing_text_returns_empty_set():
    assert extract_skills(None) == set()