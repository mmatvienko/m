from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tinydb import TinyDB, Query

import json
import credentials as C

from nltk.sentiment.vader import SentimentIntensityAnalyzer


class TwitterStream():
    """
    allows the user to stream from twitter using a 
    sentiment listener.
    topics: list that takes topics to be listened to
    """
    def __init__(self, topics=[]):
        self.listener = SentimentListener()
        self.topics = topics
        auth = OAuthHandler(C.API_KEY, C.API_SECRET_KEY)
        auth.set_access_token(C.ACCESS_TOKEN, C.ACCESS_TOKEN_SECRET)
        self.stream = Stream(auth, self.listener)

    def filter(self):
        self.stream.filter(track=self.topics)


class SentimentListener(StreamListener):
    """
    a listener that outputs sentiment data
    p much runs in infinite loop. best to write data to DB
    and then read from application that needs the data.
    """
    def __init__(self):
        self.anal = SentimentIntensityAnalyzer()
        self.db = TinyDB('./sentiment.json')
        self.key = 0
        
    def on_data(self, data):
        # do what we want with data
        data_obj = json.loads(data)

        # do sentiment analysis
        # get hashtag dict. ==> data_obj['entities']['hashtags']
        text = data_obj['text']
        analed = self.anal.polarity_scores(text)
        analed['key'] = self.key
        self.db.insert(analed)
        self.key += 1

        return True
    
    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    t = TwitterStream(topics=['finance', 'money','business','investment','trading'])
    # json.decoder.JSONDecodeError: Extra data: line 1 column 50076 (char 50075)
    t.filter()
