import twikit as tw
import asyncio
from libs.fields import selected_tweet_attributes as sta, selected_user_attributes as sua
import csv
from libs.extractors import extract_tweets
import os




client = tw.Client(language="en-US")

"""
#login

async def auth():    
    auth1 = "bexemip525@abatido.com"
    auth2 = "bexemip"
    password = "abcd1234?@"
    await client.login(auth_info_1=auth1, auth_info_2=auth2, password=password)
    client.save_cookies("private/cookies.json")
asyncio.run(auth())
"""

#load cookies
client.load_cookies("private/cookies.json")

tweets_path = "tweets.csv"
users_path = "users.csv"

if not os.path.exists(tweets_path):
    with open(tweets_path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(sta)
    print("[File Created] Tweets file created as ", tweets_path)
else:
    print(f"[Exists] Tweets path ({tweets_path}) already exists")


if not os.path.exists(users_path):        
    with open(users_path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(sua)
    print("[File Created] Users file created as ", users_path)
else:
    print(f"[Exists] Users path ({users_path}) already exists")

inputs = []
try:
    with open("inputs.txt", 'r') as file:
        inputs = file.read().splitlines()
except:
    print("[File missing] inputs.txt file is missing. Please read the README file.")
    exit(0)

try:
    count = int(inputs[0])
    query_strings = inputs[1:]
except:
    print("[Format Error] Please correct input.txt file to the correct format. Please read the README file.")
    exit(0)

i = 0
while i < (len(query_strings)):
    try:
        print(f"===={query_strings[i]}====================================================")
        print("Searching query string: ", query_strings[i])
        asyncio.run(extract_tweets(query_strings[i], count, [tweets_path, users_path], client))
        print("========================================================", end="")
        print("="*len(query_strings[i]))

    except Exception as e:
        #print("Error(main): ", e)
        continue

    i+=1






