from dotenv import load_dotenv
load_dotenv()
import os
import requests
import json
from urllib.parse import quote_plus
from requests_oauthlib import OAuth1

api_url = 'https://api.twitter.com/1.1/statuses/update.json'

def select_tweet():
    # TODO: get tweet from somewhere (local text file for now)
    # TODO: check if tweet has been used already (check tweet history of user? erase from text file?)
        # TODO: keep list of used tweets in DB?
    # TODO: check character limit
    
    return 'this is a test tweet'


# select a tweet 
status = select_tweet()


# send tweet
data_url = api_url + f"?status={quote_plus(status)}"
auth = OAuth1(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_KEY_SECRET"), os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
r = requests.post(data_url, auth=auth)

print(r.content)
