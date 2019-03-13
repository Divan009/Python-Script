import tweepy
from textblob import TextBlob

consumer_key = 'DIk02xbIDXeqfSESHvJfPoRGd'
consumer_secret = 'GMqst3z5UirXrUeSLPa9nZfJwn5Um9hKDy2vQNqkDr6odUKEJP'

access_token = '1953208724-fwKTzTEfQ8UZ9Cmu4GNH7hKwSNWnqHWTzS7vkBF'
access_token_secret = '7qw4FTvbjKLnlCNNYcDFBvJxY2WCMlBq1Od1pJocFF8mL'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Surgicalstrike2')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
user = api.get_user('twitter')
print (user.screen_name)
print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)
