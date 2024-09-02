# Load data into a PostgreSQL Data Warehouse
import sqlalchemy
import yaml
from sqlalchemy import create_engine

def read_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def get_engine():
    config = read_config()
    engine_url = f"postgresql://{config['postgresql']['user']}:{config['postgresql']['password']}@{config['postgresql']['host']}:{config['postgresql']['port']}/{config['postgresql']['database']}"
    return create_engine(engine_url)

def load_data(data):
    engine = get_engine()
    with engine.connect() as connection:
        for record in data:
            connection.execute(
                "INSERT INTO etl_table (column_name) VALUES (%s)",
                (record['column_name'],)
            )

if __name__ == "__main__":
    sample_data = [{"column_name": "cleaned value"}]
    load_data(sample_data)
