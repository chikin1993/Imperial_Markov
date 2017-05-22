'''
+++++++++Markov 40k +++++++++
A Twitter bot created to generate quotes from different races in the 40k universe using a markov chain model

This script is to tweet news made from the markov_generator.py file
'''

# Importing needed modules, tweepy for twitter api, time for delays and news for news
import tweepy
import time
import markov_generator
import os

# Getting API keys from the Heroku environ
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# A cheeky while loop do the tweets
while True:
    tweet = str(markov_generator.tweet_quote())
    api.update_status(status=tweet)
    print(tweet)
    time.sleep(18000)
