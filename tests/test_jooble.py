from src.jooble import clean_snippet


def test_removes_html_tags():
    assert clean_snippet("We need <b>Python</b> skills") == "We need Python skills"


def test_converts_nbsp_and_trims():
    assert clean_snippet("&nbsp;...hello world...&nbsp;") == "...hello world..."


def test_collapses_extra_spaces_and_newlines():
    assert clean_snippet("one   two\n\nthree") == "one two three"


def test_missing_text_gives_empty_string():
    assert clean_snippet(None) == ""