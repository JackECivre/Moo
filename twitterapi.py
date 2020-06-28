from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import twitter_credentials
from save_on_file import save_on_file

# # # # TWITTER STREAMER # # # #
class TwitterStreamer:
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_file, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API

        listener = StdOutListener(fetched_tweets_file)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_file):
        super().__init__()
        self.fetched_tweets_filename = fetched_tweets_file

    def on_data(self, data):

        global write_time, write_location, write_url, write_text, write_fulltext,\
            full_text, time ,location , url , text, screen_name, user

        try:
            tweet = json.loads(data)
            print("-----     Tweet     -----")
            print(tweet)
            print()

            try:
                time = tweet['created_at']
                write_time = "Time = " + str(time)
                print(write_time)
            except Exception as Error:
                print("Time Error: " + str(Error))

            try:
                user_data = tweet['user']
                user = user_data['name']
                screen_name = user_data['screen_name']
                location = user_data['location']
                write_location = "User = " + str(user) + "\nScreen Name = @" + str(screen_name) + " from " + str(
                    location)
                print(write_location)
            except Exception as Error:
                print("User Name Error: \n" + str(Error))

            try:
                text = tweet['text']
                print("------------------------")
                write_text = "Text = " + str(text)
                print(write_text)
                print("------------------------")
            except Exception as Error:
                print("User Name Error: \n" + str(Error))

            try:
                rt_data = tweet['retweeted_status']
                ext_text = rt_data['extended_tweet']
                full_text = ext_text['full_text']
                write_fulltext = "Full Text = " + str(full_text)
                print(write_fulltext)
            except Exception as Error:
                print("Extended Text Error: \n" + str(Error))

            try:
                rt_data = tweet['retweeted_status']
                entities = rt_data['entities']
                url_data = entities['urls']
                url_list = url_data[0]
                url = url_list['url']
                write_url = "URL = " + str(url)
                print(write_url)
            except Exception as Error:
                print("URL Error: " + str(Error))

            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

            try:
                save_on_file(self.fetched_tweets_filename, write_time, write_location, write_url, write_text,
                             write_fulltext, tweet)
            except Exception as Error:
                print("Save on file Error= "+ str(Error))

            return True

        except BaseException as e:
            print("Error on_data is = " + str(e))
        return True

    def on_error(self, status):
        print("On Error status is" + str(status))

if __name__ == '__main__':

    # Authenticate using config.py and connect to Twitter Streaming API.
    tracking_List = ["yahudi", "yahudiler", "musevi", "museviler"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, tracking_List)
