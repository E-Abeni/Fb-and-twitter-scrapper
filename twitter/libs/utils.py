from random import randint
import time
from libs.parser import parse_tweet, parse_user
import csv
import os

async def get_comments(results):
    if results is None:
        results = None
    else:
        wait_time = randint(5, 10)
        print(f'[Sleep] - Fetching tweets after {wait_time} seconds ...')
        time.sleep(wait_time)
        results = await results.next()

    return results


async def get_tweets(results, query, client):
    if results is None:
        print(f'[Fetch] - Fetching tweets...')
        results = await client.search_tweet(query, product='Top')
    else:
        wait_time = randint(5, 10)
        print(f'[Sleep] - Fetching tweets after {wait_time} seconds ...')
        time.sleep(wait_time)
        results = await results.next()

    return results

import pandas as pd

def write_tweet(tweet, path):
    tweet_obj = parse_tweet(tweet)

    tweet_df = pd.DataFrame([tweet_obj])

    if os.path.exists(path):
        existing_df = pd.read_excel(path)
        existing_df = pd.concat([existing_df, tweet_df], ignore_index=True)
    else:
        existing_df = tweet_df

    existing_df.to_excel(path, index=False)

"""
# Write to CSV file. changed to xslx to handle amharic characters

def write_tweet(tweet, path):
    tweet_obj = parse_tweet(tweet)

    
    with open(path, 'a', newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(tweet_obj)

        except Exception as e:
            #print("Error: ", tweet)
            pass

            """"""
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
            """"""

    return 0
"""

def write_user(user, path):
    user_obj = parse_user(user)

    user_df = pd.DataFrame([user_obj])

    if os.path.exists(path):
        existing_df = pd.read_excel(path)
        existing_df = pd.concat([existing_df, user_df], ignore_index=True)
    else:
        existing_df = user_df

    existing_df.to_excel(path, index=False)

    return 0

"""
# Write to CSV file. changed to xslx to handle amharic characters
def write_user(user, path):
    user_obj = parse_user(user)

    with open(path, 'a', newline='', encoding="utf-8") as file:
        try:
            writer = csv.writer(file)
            writer.writerow(user_obj)

        except Exception as e:
            print("Error: ", user)

"""

