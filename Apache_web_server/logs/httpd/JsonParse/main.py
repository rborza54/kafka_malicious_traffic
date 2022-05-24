from kafka import KafkaConsumer, KafkaProducer
import os
import json
from datetime import datetime


broker = os.environ.get('broker')
my_logs = os.environ.get('my_logs')
source = os.environ.get('source')
destination = os.environ.get('destination')

def unix_time (data:str, tz:str ) -> float:


    try : 
        d = datetime.strptime(data+" "+tz, "%d/%b/%Y:%H:%M:%S %z")
    except:
        print ("format data incorect")
        return 0
    return int(d.timestamp())

def ApacheLog( log : str ) -> dict:


    try:

        array = log.split()

        format = {

            "IP": array[0],
            "Time": unix_time(array[3][1:], array[4][:-1]),
            "Request Method": array[5][1:],
            "Request Resource": array[6],
            "Request Protocol": array[7][-1],
            "Status Code": int(array[8]),
            "Payload Size": int(array[9]),
            "Referer": array[10]. replace("\"", ""),
            "User Agent": " ".join(array[11:]).replace("\"", "")
        }

        return format

    except ValueError:
        print (" FORMAT LOG TYPE INCORECT")
        return {}
    except IndexError:  
        print("INCORRECT LOG STRING")
        return {}
    except AttributeError:
        print("log prea lung/prea scurt")
        return {}

if __name__ == "__main__":
    consumer = KafkaConsumer(
        source,
        bootstrap_servers = broker,
        value_deserializer = lambda value: json.loads(value),
        consumer_timeout_ms = 5000

    )
    
    producer = KafkaProducer(
        bootstrap_servers = broker,
        value_serializer = lambda value: json.dumps(value).encode(),
    )

    

    for message in consumer :

        errors = 0 
        

        info : dict = \
            ApacheLog (message.value["line"])
        if info != {} and info['Time'] != 0:
            producer.send(destination, value = info)
        else:
            errors = 1


