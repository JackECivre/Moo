

def clear_tweet(tweet_desired_data):
    try:
        tweet_desired_data["full_text"] = ""
        tweet_desired_data["language"] = ""
        tweet_desired_data["user"] = ""
        tweet_desired_data["text"] = ""
        tweet_desired_data["url"] = ""
        tweet_desired_data["time"] = ""
        tweet_desired_data["screen_name"] = ""
        tweet_desired_data["location"] = ""
        tweet_desired_data["write_location"] = ""
        tweet_desired_data["write_time"] = ""
        tweet_desired_data["write_url"] = ""
        tweet_desired_data["write_text"] = ""
        tweet_desired_data["write_fulltext"] = ""

    except Exception as Error:
        print("Data Clearing Problem = " + str(Error))

    return tweet_desired_data
