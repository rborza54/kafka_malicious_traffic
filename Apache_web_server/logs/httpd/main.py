from kafka import KafkaProducer 
import json
import os

broker = os.environ.get('broker')
open_topic = os.environ.get('open_topic')
my_logs = os.environ.get('my_logs')



if __name__ == '__main__': 
    producer = KafkaProducer (
        bootstrap_servers = broker,
        value_serializer = lambda value: json.dumps(value).encode(),
    )

   
    
    with open ('other_vhosts_access.log') as logs :
        
        for line in logs :


            log : dict = {'line' : line }
            producer.send(open_topic, value = log)

            
