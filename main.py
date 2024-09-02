import facebook
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("access_token")

graph = facebook.GraphAPI(access_token=access_token, version='2.8')

try:
    friends = graph.get_object('me/', fields='id, name, email')
    print(friends)
except facebook.GraphAPIError as e:
    print(f'Error: {e}')