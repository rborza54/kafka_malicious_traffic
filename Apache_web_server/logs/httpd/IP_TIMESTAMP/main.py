from kafka import KafkaConsumer, KafkaProducer
import json
import os
import time


broker = os.environ.get("broker")
source = os.environ.get("source")
destination = os.environ.get("destination")


def function( info: dict) -> dict: 

    try:

        array = {
            "IP": info ['IP'],
            "TS": info ['Time'],
        }

        return array

    except KeyError:
        return {}



if __name__ == "__main__":
    consumer = KafkaConsumer(
        source,
        bootstrap_servers = broker,
        value_deserializer = lambda value: json.loads(value),
        consumer_timeout_ms = 5000
    )

    producer = KafkaProducer (
        bootstrap_servers = broker,
        value_serializer = lambda value: json.dumps(value).encode(),
    )


    
    erori = 0
    start = time.time()


    for message in consumer :

        

        info_ip_ts : dict = function(message.value)
        if info_ip_ts != {}:
            producer.send(destination, value = info_ip_ts)
        else:
            erori += 1

        
        