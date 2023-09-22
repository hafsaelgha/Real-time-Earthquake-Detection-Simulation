import json
from time import sleep
from json import dumps
from kafka import KafkaProducer
import json

topic_name='sensor_data_consumer'
producer = KafkaProducer(bootstrap_servers=['52.87.254.233:9092']
,value_serializer=lambda x: dumps(x).encode('utf-8'))

def lambda_handler(event, context):
    print(event)
    payload_part=json.loads(event['body'])['payload']
    for i in payload_part:
        light_illumination=i['values']['lux']
        capture_time=i['time']
        data={"light_illumination":light_illumination,"capture_time":capture_time}
        print(data)
        producer.send(topic_name, value=data)
    producer.flush()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
