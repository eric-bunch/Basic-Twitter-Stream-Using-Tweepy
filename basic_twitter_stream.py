# Tweepy stuff
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import json


class listener(StreamListener):	

	def on_data(self, data):		
		try:
			json_data = json.loads(data)
			tweet = json_data['text']
			print "TWEET: ",tweet,'\n'
			return True			
		except BaseException as e:
			print 'failed ondata', str(e)
			time.sleep(5)
			
		def on_error(self, status):
			print status


ckey = ''
csecret = ''
atoken = ''
asecret = ''

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
