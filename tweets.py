import tweepy

consumer_key = 'EnterYourOwn'
consumer_secret = 'EnterYourOwn'

access_token = 'EnterYourOwn'
access_token_secret = 'EnterYourOwn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('crypto')

for tweet in public_tweets:
	print(tweet.text)