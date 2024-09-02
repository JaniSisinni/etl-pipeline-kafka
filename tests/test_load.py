#Unit test for load step
import pytest
from unittest.mock import patch, MagicMock
from load.data_loader import load_data, get_engine

@pytest.fixture
def sample_data():
    return [
        {"column_name": "cleaned value"},
        {"column_name": "123"}
    ]

@patch('load.data_loader.get_engine')
def test_load_data(mock_get_engine, sample_data):
    # Mock the SQLAlchemy engine and connection
    mock_engine = MagicMock()
    mock_connection = MagicMock()
    mock_get_engine.return_value = mock_engine
    mock_engine.connect.return_value.__enter__.return_value = mock_connection

    # Call the load_data function with sample data
    load_data(sample_data)

    # Assert the connection execute method was called with expected SQL and data
    calls = [
        (("INSERT INTO etl_table (column_name) VALUES (%s)", ("cleaned value",)),),
        (("INSERT INTO etl_table (column_name) VALUES (%s)", ("123",)),)
    ]
    mock_connection.execute.assert_has_calls(calls, any_order=True)

if __name__ == "__main__":
    pytest.main()
