import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(filepath_or_buffer='max_latency_result.csv', header=None)
df.columns = ['topic_name', 'latency', 'consumer_number']
df['topic_and_consumer_number'] = df['topic_name'] + '_' + df['consumer_number'].astype(str)
df = df.groupby('topic_name', as_index=False).max('latency')
df = df.sort_values(by=['topic_name'], ascending=False)

plt.figure(figsize=(10, 10))
plt.plot(df['latency'], df['topic_name'], label='Latency')
plt.title('Max Latency by Topic Name')
plt.show()
plt.savefig('max_latency_plot.png')
