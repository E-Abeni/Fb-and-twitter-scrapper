import twikit as tw
import asyncio
from fields import selected_tweet_attributes as sta
import csv
from extractors import extract_tweets



client = tw.Client(language="en-US")
client.load_cookies("cookies.json")

main = "tweets.csv"
comment = "comments.csv"

"""
with open(main, 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(sta)

with open(comment, 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(sta)
"""

done = []
query_strings = ["Ethiopia", "Amhara", "Tigray", "Oromo", "Sidama", "Gurage"]

i = 0

while i < (len(query_strings)):
    try:
        print("Searching query string: ", query_strings[i])
        asyncio.run(extract_tweets(query_strings[i], 200, [main, comment], client))

    except:
        continue

    i+=1


























"""    
def tweet_to_list(tweet):
    tweet_obj = []
    print("=============================================================")
    print(tweet)
    for attr in sta:
        if attr == "user":
            tweet_obj.append(str(tweet.__getattribute__(attr).id))
            continue
        try:
            value = tweet.__getattribute__(attr)
        except:
            value = tweet.__getattribute__(attr).encode("utf-8")

        if type(value) == type(None):
            tweet_obj.append("-")
        elif type(value) == type(True):
            tweet_obj.append(str(value))
        elif type(value) == type(3):
            tweet_obj.append(str(value))
        elif type(value) == type([]):
            tweet_obj.append("list")
        else:
            tweet_obj.append(value)
        
    return tweet_obj
"""
