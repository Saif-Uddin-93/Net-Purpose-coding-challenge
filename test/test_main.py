import pytest
from src.main import get_results


given_division = [
    {
        "name": "Rockets",
        "points": 64,
    },
    {
        "name": "Cardinals",
        "points": 77,
    },
    {
        "name": "Bruisers",
        "points": 51,
    },
    {
        "name": "Renegades",
        "points": 37,
    },
    {
        "name": "Porpoises",
        "points": 52,
    },
]


def test_returns_one_team_to_promote_and_one_team_to_relegate():
    result_string = """Promote:
Cardinals

Relegate:
Renegades"""
    assert get_results(given_division, 1) == result_string


def test_returns_two_teams_to_promote_and_two_teams_to_relegate():
    result_string = """Promote:
Cardinals
Rockets

Relegate:
Bruisers
Renegades"""
    assert get_results(given_division, 2) == result_string


def test_returns_none_if_n_value_too_large():
    with pytest.raises(Exception) as exc_info:
        get_results(given_division, 3)

    result = str(exc_info.value)
    expected = "3, is too big. Enter a number that is a maximum of, 2"

    assert result == expected


def test_returns_type_string():
    result = get_results(given_division, 2)
    assert isinstance(result, str)


def test_top_teams_with_equal_scores():
    test_division = [
        {
            "name": "Rockets",
            "points": 77,
        },
        {
            "name": "Cardinals",
            "points": 77,
        },
        {
            "name": "Bruisers",
            "points": 77,
        },
        {
            "name": "Renegades",
            "points": 37,
        },
        {
            "name": "Porpoises",
            "points": 52,
        },
    ]

    with pytest.raises(Exception) as exc_info:
        get_results(test_division, 2)

    result = str(exc_info.value)
    expected = "Too many teams in the top with the same score to promote"
    assert result == expected


def test_bottom_teams_with_equal_scores():
    test_division = [
        {
            "name": "Rockets",
            "points": 77,
        },
        {
            "name": "Cardinals",
            "points": 77,
        },
        {
            "name": "Bruisers",
            "points": 37,
        },
        {
            "name": "Renegades",
            "points": 37,
        },
        {
            "name": "Porpoises",
            "points": 37,
        },
    ]

    with pytest.raises(Exception) as exc_info:
        get_results(test_division, 2)

    result = str(exc_info.value)
    expected = "Too many teams in the bottom with the same score to relegate"

    assert result == expected


def test_all_teams_with_equal_scores():
    test_division = [
        {
            "name": "Rockets",
            "points": 77,
        },
        {
            "name": "Cardinals",
            "points": 77,
        },
        {
            "name": "Bruisers",
            "points": 77,
        },
        {
            "name": "Renegades",
            "points": 77,
        },
        {
            "name": "Porpoises",
            "points": 77,
        },
    ]

    with pytest.raises(Exception) as exc_info:
        get_results(test_division, 2)

    result = str(exc_info.value)
    expected = "All teams have the same score. Cannot promote or \
relegate any teams."

    assert result == expected


def test_average_score_77_does_not_raise_exception():
    test_division = [
        {
            "name": "Rockets",
            "points": 77,
        },
        {
            "name": "Cardinals",
            "points": 76,
        },
        {
            "name": "Bruisers",
            "points": 75,
        },
        {
            "name": "Renegades",
            "points": 78,
        },
        {
            "name": "Porpoises",
            "points": 79,
        },
    ]

    result = get_results(test_division, 2)
    expected = """Promote:
Porpoises
Renegades

Relegate:
Cardinals
Bruisers"""

    assert result == expected
