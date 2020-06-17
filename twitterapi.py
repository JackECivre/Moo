from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import twitter_credentials


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            print("-----     Tweet     -----")
            print(tweet)

            time = tweet['created_at']
            print("Time = " + str(time))

            try:
                user_data = tweet['user']
                user = user_data['name']
                location = user_data['location']
                print("User = " + str(user) + " from " + str(location))
            except Exception as Error:
                print("User Name Error: " + str(Error))

            try:
                text = tweet['text']
                print("------------------------")
                print("Text = " + str(text))
                print("------------------------")
            except Exception as Error:
                print("User Name Error: " + str(Error))

            # try:
            #     rt_data = tweet['retweeted_status']
            #     ext_text = rt_data['full_text']
            #     print("Extended Text = " + str(ext_text))
            # except Exception as Error :
            #     print("Extended Text Error: " + str(Error))
            #
            #
            # try:
            #     rt_data = tweet['extended_tweet']
            #     print("extended Tweet info is : " + rt_data)
            #     ext_text = rt_data['full_text']
            #     print("Extended Text = " + str(ext_text))
            # except Exception as Error :
            #     print("Extended Text Error: " + str(Error))
            #
            # try:
            #     entities = tweet['entities']
            #     url_data = entities['urls']
            #     url = url_data['url']
            #     print("URL = " + str(url))
            # except Exception as Error :
            #     print("URL Error: " + str(Error))

            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            print("")



            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(json.dumps(tweet))

            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.
    tracking_List = ["yahudi", "yahudiler", "musevi", "museviler", "ermeni", "ermeniler", "ibne"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, tracking_List)
