from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime

import twitter_credentials


class TwitterStreamer():
    
    def __init__(self, fetched_tweets_filename):
        super().__init__()
        self.fetched_tweets_filename = fetched_tweets_filename

    def stream_tweets(self, fetched_tweets_filename, tracking_list):
        # Handles Twitter Authentication and the connection to Twitter Streaming API
        # --------------------------------------------------------
        listener = StandartListener()
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)

        stream.filter(track=tracking_List)


class StandartListener(StreamListener):

    # Handles Streaming and Processing of live Tweets
    # --------------------------------------------------------


    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, "a") as tf:
                tf.write(data)
            return True
        except BaseException as Error:
            print("Error on data: %s" % str(Error))
            return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    tracking_List = ["yahudi", "yahudiler", "musevi", "museviler", "ermeni", "ermeniler", "ibne", "yunan"]
    fetched_tweets_filename = f"{datetime.datetime.now()}-tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, tracking_List)
