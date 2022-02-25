from json import dumps

from kombu_producer import KombuProducer

if __name__ == '__main__':
    try:
        KombuProducer(
            exchange_name="exchange1",
            exchange_type="direct",
            routing_key="key1",
            broker_url="amqp://guest:guest@localhost:5672/"
        ).publish_payload(
            payload=dumps(
                {
                    "event": "TestEvent",
                    "data": {
                        "a": "b",
                    },
                }
            )
        )
    except Exception as e:
        print(f"Unable to publish TestEvent event, Error: {e}")
    print("Published TestEvent")
