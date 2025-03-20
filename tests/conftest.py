import pytest

_value = [
    {
        "id": "3",
        "url": "mock_url",
        "primaryTitle": "Mock Title",
        "description": "mock_description",
        "primaryImage": "mock_primaryImage",
        "contentRating": "mock_R",
        "startYear": 1994,
        "endYear": None,
        "type": "Mock Type",
        "releaseDate": "1994-10-14",
        "budget": 25000000,
        "grossWorldwide": 29332133,
        "isAdult": False,
        "runtimeMinutes": 142,
        "averageRating": 9.3,
        "numVotes": 3019758,
    }
]


@pytest.fixture()
def my_mock_value():
    return _value
