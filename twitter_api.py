from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import datetime
# from save_on_text_file import save_on_text_file
from create_excel_file import create_excel_file
from clear_tweet_data import clear_tweet
from tweet_data import tweet_data
import json
import time
# from run_moo import fetched_tweets_filename

# # # # TWITTER STREAMER # # # #


class TwitterStreamer:
    """
    Class for streaming and processing live tweets.
    """

    print("Script Starting")

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_file, hash_tag_list):
        # This handles Twitter auth and the connection to Twitter Streaming API
        print("Authentication in Progress")

        listener = StdOutListener(fetched_tweets_file)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        print("Authentication Completed - Fetching Tweets")

        # This line filter Twitter Streams to capture data by the keywords:

        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_file):
        super().__init__()
        self.fetched_tweets_filename = fetched_tweets_file

    def on_data(self, data):

        # -+-+-+-+-+-Function that Gathers the desired data from Tweet Data-+-+-+-+-+-
        tweet_desired_data = {}
        try:
            tweet_json = json.loads(data)
            tweet_desired_data = tweet_data(tweet_json)
            # print("tweet_desired_Data is :" + str(tweet_desired_data))

        except Exception as Error:
            print("Tweet Data error: " + str(Error))

        now_time = str(datetime.datetime.now())

        # -+-+-+-+-+-function that saves the Tweet Data if language is desired-+-+-+-+-+-
        language = tweet_desired_data['language']

        if str(language) != "tr":
            print("Data Not Saved to file. \nLanguage is = " + str(language))
        else:
            try:
                filename_excel = self.fetched_tweets_filename + ".csv"
                create_excel_file(filename_excel, tweet_desired_data, now_time)

            except Exception as Error:
                print("Save on Excel file Error = " + str(Error))

            # -+-+-+-+-+-function that clears data for the next tweet-+-+-+-+-+-
        try:
            clear_tweet(tweet_desired_data)
        except Exception as Error:
            print("Clear Tweet Error " + str(Error))

    def on_error(self, status):
        print("On Error status is " + str(status))
        if status == 420:
            # returning False in on_error disconnects the stream
            return False


def handle_exception():
    print("Something Crushed MOO !!!")
    pass


def moo():
    try:
        if __name__ == '__main__':
            # Authenticate using config.py and connect to Twitter Streaming API.
            tracking_list = ["yahudi", "yahudiler", "musevi", "museviler", "sinagog", "sinagoglar", "havra", "haham",
                             "hahamlar", "holokost"]
            fetched_tweets_filename = str(datetime.date.today())
            print(fetched_tweets_filename)

            twitter_streamer = TwitterStreamer()
            twitter_streamer.stream_tweets(fetched_tweets_filename, tracking_list)
    except Exception as Error:
        print("App Error re-trying " + str(Error))
        time.sleep(10)
        moo()
        handle_exception()


moo()
