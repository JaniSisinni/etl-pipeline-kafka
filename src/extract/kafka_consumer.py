#Extract data from Kafka
from kafka import KafkaConsumer
import json
import yaml

def read_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def consume_messages():
    config = read_config()
    consumer = KafkaConsumer(
        config['kafka']['topic'],
        bootstrap_servers=config['kafka']['bootstrap_servers'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='etl_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        yield message.value

if __name__ == "__main__":
    for message in consume_messages():
        print(f"Received message: {message}")
