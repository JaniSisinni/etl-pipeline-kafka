#Orchestration of the ETL process
from extract.kafka_consumer import consume_messages
from transform.data_transformer import transform
from load.data_loader import load_data

def main():
    for message in consume_messages():
        transformed_data = transform(message)
        load_data(transformed_data)

if __name__ == "__main__":
    main()
