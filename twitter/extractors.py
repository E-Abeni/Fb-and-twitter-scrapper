import twikit as tw
from datetime import datetime
import time
from utils import write_tweet, get_tweets, get_comments

async def extract_tweets(query, TWEET_COUNT, path, client):
    
    count = 0
    results = None
    
    while count < TWEET_COUNT:
        try:
            results = await get_tweets(results, query, client)
        except tw.TooManyRequests as e:
            rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
            print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
            wait_time = rate_limit_reset - datetime.now()
            time.sleep(wait_time.total_seconds())
            continue

        if not results:
            print(f'{datetime.now()} - No more tweets found')
            break

        for tweet in results:
            count += 1
            write_tweet(tweet, path[0])
            await extract_comments(tweet.replies, 50, path[1])
            await extract_related_tweets(tweet.related_tweets, path[0])

        print(f'{datetime.now()} - Got {count} tweets')

    print(f'{datetime.now()} - Done! Got {count} tweets found')    

    return count



async def extract_comments(results, COMMENT_COUNT, path):
    count = 0
        
    while count < COMMENT_COUNT and results:

        for tweet in results:
            count += 1
            write_tweet(tweet, path)
        
        try:
            results = await get_comments(results)
        except tw.TooManyRequests as e:
            rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
            wait_time = rate_limit_reset - datetime.now()
            time.sleep(wait_time.total_seconds())
            continue

        if not results:
            break

    return count


async def extract_related_tweets(tweet_list, path):
    if not tweet_list:
        return 0
    for tweet in tweet_list:
        write_tweet(tweet, path)
