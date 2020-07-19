from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import datetime
from save_on_text_file import save_on_text_file
from save_on_excel_file import save_on_excel_file
from clear_tweet_data import clear_tweet
from save_on_excel_line import save_line
from tweet_data import tweet_data
import json


# # # # TWITTER STREAMER # # # #


class TwitterStreamer:
    """
    Class for streaming and processing live tweets.
    """

    print("Script Starting")

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_file, hash_tag_list):

        # This handles Twitter authetification and the connection to Twitter Streaming API
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
            tweet = json.loads(data)
            tweet_desired_data = tweet_data(tweet)
            # print("tweet_desired_Data is :" + str(tweet_desired_data))

        except Exception as Error:
            print("Tweet Data error: " + str(Error))

        # -+-+-+-+-+-function that saves the desired data into a text file-+-+-+-+-+-
        now_time = str(datetime.datetime.now())

        # -+-+-+-+-+-function that creates and saves the EMPTY Excel file-+-+-+-+-+-
        filename_excel = self.fetched_tweets_filename + ".xlsx"
        save_on_excel_file(filename_excel)

        # -+-+-+-+-+-function that saves the Tweet Data if language is not Endonesian or Portugesse-+-+-+-+-+-
        language = tweet_desired_data['language']

        if str(language) == "in":
            print("Data Not Saved to file. \nLanguage is = " + str(language))
        elif str(language) == "pt":
            print("Data Not Saved to file. \nLanguage is = " + str(language))
        else:
            try:
                filename_text = self.fetched_tweets_filename + ".txt"
                save_on_text_file(filename_text, tweet_desired_data, now_time, tweet)
            except Exception as Error:
                print("Save on Text file Error = " + str(Error))

            try:
                line_no = 1
                print("line_no_d: " + str(line_no))

                line_no += 1
                print("line_no_e: " + str(line_no))
            except Exception as Error:
                print("Save on Excel file Error = " + str(Error))

            # try:
            #     save_line(line_no, col, worksheet, now_time, time, username, location, text, full_text, url)
            #     print("Row Number is:" + str(line_no))
            # except Exception as Error:
            #     print("Save Line Error is : " + str(Error))

            # -+-+-+-+-+-function that clears data for the next tweet-+-+-+-+-+-
        try:
            tweet_desired_data = clear_tweet(tweet_desired_data)
            # print("CLEARED tweet_desired_data is " + str(tweet_desired_data))
        except Exception as Error:
            print("Clear Tweet Error " + str(Error))

    def on_error(self, status):
        print("On Error status is " + str(status))


if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.
    tracking_List = ["yahudi", "yahudiler", "musevi", "museviler", "sinagog", "havra", "haham"]
    fetched_tweets_filename = "tweet"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, tracking_List)
