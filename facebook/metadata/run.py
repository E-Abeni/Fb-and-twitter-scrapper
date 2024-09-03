"""
Author: Abenezer tamirat

"""

import facebook
from dotenv import load_dotenv
import os
import genMetadata

#loading the api keys from local environment variables
load_dotenv()
app_secret = os.getenv("app_secret")
app_id = os.getenv("app_id")
access_token = os.getenv("access_token")


#create graph api object to query facebook api with my app secret keys
graph = facebook.GraphAPI(access_token=access_token, version='2.8')

#generate all the metadata of available api routes (or nodes) recursively.
#It stores any metadata to facebook/m_data
#It stores the data of every api route it encounters in to facebook/data

genMetadata.generateMetadata("/me/", graph, file_name="/user_metadata")


