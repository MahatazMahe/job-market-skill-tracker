from src.roles import is_relevant_title


def test_data_engineer_is_relevant():
    assert is_relevant_title("Senior Data Engineer") is True


def test_full_stack_engineer_is_relevant():
    assert is_relevant_title("Full Stack Engineer – Technical Lead") is True


def test_case_does_not_matter():
    assert is_relevant_title("MACHINE LEARNING ENGINEER") is True


def test_mechanical_engineer_is_not_relevant():
    assert is_relevant_title("Mechanical Test Engineer") is False


def test_missing_title_is_not_relevant():
    assert is_relevant_title(None) is False