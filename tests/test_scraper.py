import pytest
import unittest.mock as mock
from etl_pipeline.src import web_scraper


@mock.patch("etl_pipeline.src.web_scraper.fetch_top250_movies")
def test_fetch_top250_movies(mock_data,my_mock_value):
    mock_data.return_value = my_mock_value
    data = web_scraper.fetch_top250_movies()
    assert data == my_mock_value



