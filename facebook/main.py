import facebook
from dotenv import load_dotenv
import os
import json

load_dotenv()
app_secret = os.getenv("app_secret")
app_id = os.getenv("app_id")
access_token = os.getenv("access_token")

graph = facebook.GraphAPI(access_token=access_token, version='2.8')

try:
    friends = graph.get_object('me/', metadata="1", fields='')
    with open("user_metadata.txt", "w") as file:
        json.dump(friends, file, indent=4)
except facebook.GraphAPIError as e:
    print(f'Error: {e}')

#help("facebook")