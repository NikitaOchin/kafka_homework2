import time

from main import main
from multiprocessing import Process

variance = [('subreddit_0', 1, 1, 1,),
            ('subreddit_1', 1, 2, 1,),
            ('subreddit_2', 2, 2, 1,),
            ('subreddit_3', 5, 5, 1,),
            ('subreddit_4', 10, 1, 1,),
            ('subreddit_5', 10, 5, 1,),
            ('subreddit_6', 10, 10, 1,),
            ('subreddit_7', 10, 10, 2,)]

if __name__ == '__main__':
    for params in variance:
        proccess = Process(target=main, args=params)
        proccess.start()
        proccess.join()
