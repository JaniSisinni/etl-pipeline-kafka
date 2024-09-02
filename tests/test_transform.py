#Unit test for tranform step

import pytest
from transform.data_transformer import clean_data, validate_data, transform

def test_clean_data():
    # Example input data with dirty values
    input_data = [
        {"column_name": " dirty value "},
        {"column_name": None},
        {"column_name": "123"},
        {"column_name": " "},  # An empty space that should be cleaned
        {"column_name": "456"}
    ]
    
    # Cleaned data should strip spaces and drop None and empty values
    expected_output = [
        {"column_name": "dirty value"},
        {"column_name": "123"},
        {"column_name": "456"}
    ]
    
    cleaned_data = clean_data(input_data)
    assert cleaned_data == expected_output, f"Expected {expected_output} but got {cleaned_data}"

def test_validate_data():
    # Example valid data
    valid_data = [
        {"column_name": "cleaned value"},
        {"column_name": "123"}
    ]
    
    # Data should pass validation
    assert validate_data(valid_data) == True
    
    # Example invalid data (with None)
    invalid_data = [
        {"column_name": "cleaned value"},
        {"column_name": None}
    ]
    
    with pytest.raises(AssertionError):
        validate_data(invalid_data)

def test_transform():
    # Example input data
    input_data = [
        {"column_name": " dirty value "},
        {"column_name": "123"},
        {"column_name": "456"}
    ]
    
    # Expected transformed data after cleaning and validation
    expected_output = [
        {"column_name": "dirty value"},
        {"column_name": "123"},
        {"column_name": "456"}
    ]
    
    transformed_data = transform(input_data)
    assert transformed_data == expected_output, f"Expected {expected_output} but got {transformed_data}"

if __name__ == "__main__":
    pytest.main()
