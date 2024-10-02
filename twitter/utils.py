from random import randint
from datetime import datetime
import time
from parser import parse_tweet
import csv

async def get_comments(results):
    if results is None:
        results = None
    else:
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds ...')
        time.sleep(wait_time)
        results = await results.next()

    return results


async def get_tweets(results, query, client):
    if results is None:
        print(f'{datetime.now()} - Getting tweets...')
        results = await client.search_tweet(query, product='Top')
    else:
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds ...')
        time.sleep(wait_time)
        results = await results.next()

    return results


def write_tweet(tweet, path):
    tweet_obj = parse_tweet(tweet)

    
    with open(path, 'a', newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(tweet_obj)

        except Exception as e:
            print("Error: ", tweet)


            """
            print("------------------")
            print(e, "Length: ", len(tweet_obj))
            print("+++++++++++++++++++")
            for i in tweet_obj:
                print(i)
            print("------------------")
            
            print("+++++++++++++++++++")
            print("Lenth of tweet: ", len(tweet_obj))
            for i in tweet_obj:
                print(type(i))
            print("+++++++++++++++++++")
            """

    return 0







