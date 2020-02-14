from generatetext import getMsg
import tweepy, time
from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET  



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

i = 0
while True:
    api.update_status(getMsg())
    time.sleep(30)
    i = i+ 1