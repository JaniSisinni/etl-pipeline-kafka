#Unit testing for extraction step
from extract.kafka_consumer import consume_messages

def test_consume_messages():
    messages = consume_messages()
    assert isinstance(next(messages), dict)
