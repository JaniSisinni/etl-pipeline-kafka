# Data cleaning and validation
import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)
    # Cleaning data
    df.dropna(inplace=True)
    df['column_name'] = df['column_name'].str.strip()  # Example of string cleaning
    df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')
    df.dropna(subset=['column_name'], inplace=True)
    return df.to_dict(orient='records')

def validate_data(data):
    df = pd.DataFrame(data)
    # Validate data 
    assert df['column_name'].notnull().all(), "Column 'column_name' has null values"
    return True

#Transform data
def transform(data):
    cleaned_data = clean_data(data)
    if validate_data(cleaned_data):
        return cleaned_data
    else:
        raise ValueError("Data validation failed")

if __name__ == "__main__":
    sample_data = [{"column_name": " value "}, {"column_name": None}]
    print(transform(sample_data))
