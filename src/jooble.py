import html
import re


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