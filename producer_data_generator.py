from kafka import KafkaProducer
import time
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import json

BOOTSTRAP_SERVERS = 'localhost:19092'

class ProducerDataGenerator:
    def __init__(self, topic_name, file_url, amount_of_producer):
        self.producers = [
               KafkaProducer(
                bootstrap_servers=BOOTSTRAP_SERVERS,
                value_serializer=lambda data: json.dumps(data).encode('utf-8')
            ) for _ in range(amount_of_producer)
        ]

        self.df = pd.read_csv(file_url).head(5)
        for index, row in self.df.iterrows():
            self.producers[index % amount_of_producer].send(topic_name, row.to_dict())

        # THIS CODE ONLY FOR TEST AND IN ORDER TO EASY STOP THE PROCESS
        time.sleep(15)
        self.producers[0].send(topic_name, {'status': 'end'})



if __name__ == '__main__':
    ProducerDataGenerator('subreddit', 'kaggle_RC_2019-05.csv')
    print('ProducerDataGenerator was Created')
