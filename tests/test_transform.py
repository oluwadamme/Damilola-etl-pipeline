import pytest
import unittest.mock as mock
from etl_pipeline.src import data_transform
import polars as pl


@pytest.fixture
def mock_data(my_mock_value):
    with mock.patch("etl_pipeline.src.data_transform.transform_data") as mocked_data:
        expected_df = pl.DataFrame(my_mock_value)
        mocked_data.return_value = expected_df
        yield mocked_data


def test_transform_data(mock_data, my_mock_value):
    data = data_transform.transform_data(my_mock_value)
    assert data.equals(mock_data.return_value)
