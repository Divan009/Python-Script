import tweepy
from textblob import TextBlob

consumer_key = 'CDKMcKTZ8gzPmeG5lbAU6wrae'
consumer_secret = 'qw5rithyUvaajskAoCwWgTNEZ6oPTOCEPZI6AYuMqh5pWZ70KL'

access_token = '1953208724-PmtdPMVHcXh982HerSUOplpY3o48VmDMWWnEj4Z'
access_token_secret = 'XY5AKOdzY0PlOiNqaZzWIM3nd2PcTP1qCko6jpFSYxEWo'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
user = api.get_user('dugar_diva')
print (user.screen_name)
print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)
