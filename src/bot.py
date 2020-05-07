import tweepy
from time import sleep
import random
from credentials import * # API shtuffs

# Variables
starter = "A caption from the 6ix: "
numtweets = 5
search = "@captionsbydrake"

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file = open('CleanLyrics_Drake.txt', 'r') # Temporary source of quotes
file_lines = my_file.readlines()
my_file.close()

def get_quote():
	export = random.choice(file_lines)
	print(starter + export)
	return export

for tweet in tweepy.Cursor(api.search, search).items(numtweets):	
	try:
		tweetID = tweet.user.id
		username = tweet.user.screen_name
		caption = get_quote()
		api.update_status("@" + username + " " + caption, in_reply_to_status_id = tweetID)
		print("Replied to " + username + " with " + caption)
	except tweepy.TweepError as e: 
		print(e.reason)
	except StopIteration:
		break