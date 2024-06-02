import sys

from kafka.admin import KafkaAdminClient, NewTopic
from producer_data_generator import ProducerDataGenerator
from consumer_data_receiver import ConsumerDataReceiver
from multiprocessing import Process

def topic_creation(topic_name, num_partitions):
    admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:19092",
        client_id='my_admin'
    )

    topic_list = [NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=1)]
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

    admin_client.close()


def main(topic_name, num_partitions, num_consumer, amount_of_producer):
    try:
        topic_creation(topic_name, num_partitions)
        print('Topic Created')
    except Exception as e:
        print(f'Topic {topic_name} already exists')

    Process(target=ProducerDataGenerator, args=(topic_name, 'kaggle_RC_2019-05.csv', amount_of_producer, )).start()
    for num in range(num_consumer):
        Process(target=ConsumerDataReceiver, args=(topic_name, num, )).start()




if __name__ == '__main__':
    main('subreddit', 1, 1, 1)

