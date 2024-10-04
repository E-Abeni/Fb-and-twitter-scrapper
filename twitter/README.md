Author: @Abenezer_Tamirat
Date: Oct-03-2024 G.C

Purpose:
	This Script will scrap tweets from X (formerly twitter). It uses twikit library to interact with twitter. It does use the standard API but scraps responses by making http requests.

Usage:
	1. First provide credentials in login_info.txt file separated by new line:
		- First line : email
		- Second line : username
		- Third line : password

	2. Then edit the input.txt file to specify search queries and how many tweets to fetch for each search query
		- First line : count of tweets for each query (must be a number)
		- Other lines: Any query strings separated by new line to search X/twitter

	3. Run the main.py file
		- It will authenticate and store session cookie at private/cookies.json file
		- This file will be used for subsequent authentications
		- Delete this file to force the script to authenticate again
		- Extracted tweets and users will be saved in tweets.csv and users.csv file for the time being

- before running the script install the dependencies listed on requirements.txt