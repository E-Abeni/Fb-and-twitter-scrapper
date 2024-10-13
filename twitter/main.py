import twikit as tw
import asyncio
from libs.fields import selected_tweet_attributes as sta, selected_user_attributes as sua
import csv
from libs.extractors import extract_tweets
import os
import pandas as pd


client = tw.Client(language="en-US")


"""Authenticate user or load existing user"""
async def auth():        
        with open("login_info.txt", "r") as file:
            login_info = file.read().splitlines()    
            await client.login(auth_info_1=login_info[0], auth_info_2=login_info[1], password=login_info[2])
            print(f"[Login] Logged in as {login_info[0]}")
        
        client.save_cookies("private/cookies.json")

if not os.path.exists("private/cookies.json"):
    asyncio.run(auth())
else:
    client.load_cookies("private/cookies.json")
    print("[Login] User already logged in")


"""
#Checkes and creates path to store the fetched tweets
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
"""


# Changed to xslx in order to handle Amharic characters
tweets_path = "tweets.xlsx"
users_path = "users.xlsx"

if not os.path.exists(tweets_path):
    df = pd.DataFrame([sta])
    df.to_excel(tweets_path, index=False)
    print("[File Created] Tweets file created as ", tweets_path)
else:
    print(f"[Exists] Tweets path ({tweets_path}) already exists")


if not os.path.exists(users_path):
    df = pd.DataFrame([sua])
    df.to_excel(users_path, index=False)
    print("[File Created] Users file created as ", users_path)
else:
    print(f"[Exists] Users path ({users_path}) already exists")



"""Loads query strings"""
inputs = []
try:
    with open("inputs.txt", 'r', encoding="utf-8") as file:
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



"""run the scrapper to extract tweets for every query string"""
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






