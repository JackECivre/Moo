from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import twitter_credentials
import datetime
from save_on_text_file import save_on_text_file
from save_on_excel_file import save_on_excel_file
from text_in_fulltext import textchecker


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

        global write_time, write_location, write_url, write_text, write_fulltext, \
            full_text, time, location, url, text, screen_name, user, language

        try:
            tweet = json.loads(data)
            print("\n-----     Tweet     -----")
            print(tweet)
            print("\n-----     Tweet Summary    -----")
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

                try:
                    ext_text = rt_data['extended_tweet']
                    full_text = ext_text['full_text']
                    write_fulltext = "Full Text = " + str(full_text) + "\n"
                    print(write_fulltext)
                except Exception as Error:
                    print("Extended Text Error: " + str(Error))

                try:
                    try:
                        entities = rt_data['entities']
                        url_data = entities['urls']
                        url_list = url_data[0]
                        url = url_list['url']
                        write_url = "URL = " + str(url)
                        print(write_url)
                    except:
                        entities = rt_data['entities']
                        url_data = entities['urls']
                        url = url_data['url']
                        write_url = "URL = " + str(url)
                        print(write_url)

                except Exception as Error:
                    print("URL Error: " + str(Error))
                    url = "Not Available"

                try:
                    textchecker(full_text, text)
                except Exception as Error:
                    print("Full Text Check Error is : " + str(Error))
                    full_text = "Not Available"

            except Exception as Error:
                print("Re-tweet Error: " + str(Error))
                full_text = None
                url = None
                write_fulltext = "Full Text = Not Available"
                write_url = "URL = Not  Available"

            try:
                language = tweet['lang']
            except Exception as Error:
                print("Language Error: " + str(Error))

            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

        except BaseException as e:
            print("Error on_data is = " + str(e))

            # -+-+-+-+-+-function that saves the desired data into a text file-+-+-+-+-+-
        now_time = str(datetime.datetime.now())


        if language == "in":
            print("Data Not Saved to file. \nLanguage is = " + str(language))
        else:
            try:
                filename_text = self.fetched_tweets_filename + ".txt"
                save_on_text_file(filename_text, now_time, write_time, write_location, write_url,
                                  write_text, write_fulltext, tweet)
            except Exception as Error:
                print("Save on Text file Error = " + str(Error))

            try:
                line_no = 1
                print("line_no_d: " + str(line_no))

                filename_excel = self.fetched_tweets_filename + ".xlsx"
                save_on_excel_file(filename_excel, now_time, full_text, time, location, url, text,
                                   screen_name, line_no)
                line_no += 1
                print("line_no_e: " + str(line_no))
            except Exception as Error:
                print("Save on Excel file Error = " + str(Error))



            # -+-+-+-+-+-function that clears data for the next tweet-+-+-+-+-+-
        try:
            full_text = ""
            text = ""
            url = ""
            time = ""
            screen_name = ""
            location = ""
            user = ""
            language = ""
        except Exception as Error:
            print("Data Clearing Problem = " + str(Error))

        return True

    def on_error(self, status):
        print("On Error status is " + str(status))


if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.
    tracking_List = ["yahudi", "yahudiler", "musevi", "museviler", "sinagog", "havra", "haham"]
    fetched_tweets_filename = "tweet"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, tracking_List)

