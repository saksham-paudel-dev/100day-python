
import pytest
from pydantic import ValidationError

from day8 import parse_ai_response


def test_valid_ai_response():
    raw = """
    {
        "name": "Saksham",
        "age": 20,
        "skills": ["Python", "SQL"]
    }
    """

    result = parse_ai_response(raw)

    assert result.name == "Saksham"
    assert result.age == 20
    assert result.skills == ["Python", "SQL"]


def test_age_out_of_range():
    raw = """
    {
        "name": "Saksham",
        "age": 150,
        "skills": ["Python"]
    }
    """

    with pytest.raises(ValidationError):
        parse_ai_response(raw)


def test_missing_required_field():
    raw = """
    {
        "name": "Saksham",
        "age": 20
    }
    """

    with pytest.raises(ValidationError):
        parse_ai_response(raw)


def test_invalid_json():
    raw = '{"name": "Saksham", "age": }'

    with pytest.raises(ValueError):
        parse_ai_response(raw)


def test_wrong_field_type():
    raw = """
    {
        "name": "Saksham",
        "age": "twenty",
        "skills": ["Python"]
    }
    """

    with pytest.raises(ValidationError):
        parse_ai_response(raw)
