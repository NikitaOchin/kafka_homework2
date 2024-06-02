import time
import asyncio
from kafka import KafkaConsumer
import json
import pandas as pd
import os
from multiprocessing import Process
import logging

BOOTSTRAP_SERVERS = 'localhost:19092'


class ConsumerDataReceiver:
    max_latency = 0

    def __init__(self, topic_name, num_consumer):
        self.consumer = KafkaConsumer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_deserializer=lambda data: json.loads(data.decode('utf-8')))
        self.consumer.subscribe([topic_name])
        for message in self.consumer:
            time.sleep(1)
            print(message.value)
            self.logs_data(producted_time=message.timestamp, cunsumed_time=time.time() * 1000),
            print('latency for this message is ' + str((time.time() * 1000) - message.timestamp) + ' miliseconds')

            if 'status' in message.value and message.value['status'] == 'end':
                print('The max latency was: ', str(self.max_latency) + ' miliseconds\n\n')
                self.consumer.close()
                pd.DataFrame(
                    {'topic_name': [topic_name],
                     'max_latency': [self.max_latency],
                     'Consumer Number': [num_consumer]}
                ).to_csv('max_latency_result.csv', mode='a', header=False, index=False)

    def logs_data(self, producted_time, cunsumed_time):
        message_latency = cunsumed_time - producted_time
        if self.max_latency < message_latency:
            self.max_latency = message_latency


if __name__ == '__main__':
    file_path = os.getenv('FILE_PATH', 'result_file.csv')
    num_of_consumer = os.getenv('NUMBER_OF_CONSUMER', 2)
    for i in range(num_of_consumer):
        Process(target=ConsumerDataReceiver,
                args=('subreddit', file_path,)
                ).start()
        print('Consumer was Created')
