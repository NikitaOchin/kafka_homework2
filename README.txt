Description
- kaggle_RC_2019-05.csv is a file to generate data and test it
- producer_data_generator.py is a producer who produce data to kafka
- consumer_data_receiver.py is a consumer who receive data from kafka broker and log the latency between producing and consuming message
- main.py is a script that create a new topic and run processes to produce and consume data
- app_test - is a script that run different scenarios

result saved in max_latency_result.csv with each max latency for each consumer

max_latency_plot.png is a graph that show the latency for different scenarios


HOW TO RUN A CODE
- Run app_test.py to get the same result
- When code finish - run Graphics.py to create a plot