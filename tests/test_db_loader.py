import pytest
import polars as pl
from unittest import mock
from datetime import date
import sqlalchemy
from sqlalchemy.orm import Session
from etl_pipeline.src import db_loader
from etl_pipeline.src.model import Movies, Base
from etl_pipeline.utils import utils


@pytest.fixture
def mock_session():
    mock_session = mock.MagicMock()
    mock_engine = mock.MagicMock()

    mock_session_instance = mock.MagicMock()
    mock_session.begin.return_value.__enter__.return_value = mock_session_instance

    with mock.patch(
        "etl_pipeline.utils.utils.connect_with_db",
        return_value=(mock_session, mock_engine),
    ):
        with mock.patch.object(Base.metadata, "drop_all") as mock_drop_all:
            with mock.patch.object(Base.metadata, "create_all") as mock_create_all:
                yield mock_session, mock_session_instance, mock_engine, mock_drop_all, mock_create_all


def test_load_data_typical_case(mock_session, my_mock_value):
    mock_session, mock_session_instance, mock_engine, mock_drop_all, mock_create_all = (
        mock_session
    )

    test_data = pl.DataFrame(my_mock_value)
    mock_session_instance.query.return_value.filter_by.return_value.first.return_value = (
        None
    )
    db_loader.load_data(test_data)

    mock_drop_all.assert_called_once_with(mock_engine)
    mock_create_all.assert_called_once_with(mock_engine)

    added_movie = mock_session_instance.add.call_args[0][0]
    assert isinstance(added_movie, Movies)
    assert added_movie.id == "3"
    assert added_movie.primaryTitle == "Mock Title"
    assert added_movie.budget == 25000000

    mock_session_instance.commit.assert_called_once()


def test_load_data_empty_dataframe(mock_session):
    mock_session, mock_session_instance, mock_engine, mock_drop_all, mock_create_all = (
        mock_session
    )
    test_data = pl.DataFrame([])
    db_loader.load_data(test_data)

    mock_drop_all.assert_called_once_with(mock_engine)
    mock_create_all.assert_called_once_with(mock_engine)

    mock_session_instance.add.assert_not_called()
    mock_session_instance.commit.assert_called_once()
