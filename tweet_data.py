from text_in_fulltext import textchecker


def tweet_data(tweet):
    results = {}
    try:

        print("\n-----     Tweet     -----")
        print(tweet)
        print("\n-----     Tweet Summary    -----")

        try:
            language = tweet['lang']
            print("language is :" + str(language))
            results["language"] = str(language)
        except Exception as Error:
            print("Language Error: " + str(Error))
            results["language"] = "Language is Not Available"

        try:
            time = tweet['created_at']
            write_time = "Time = " + str(time)
            print(write_time)
            results["time"] = str(time)
            results["write_time"] = str(write_time)
        except Exception as Error:
            print("Time Error: " + str(Error))
            results["time"] = "Time is Not Available"
            results["write_time"] = "Time is Not Available"

        try:
            user_data = tweet['user']
            user = user_data['name']
            screen_name = user_data['screen_name']
            location = user_data['location']
            write_location = "User = " + str(user) + "\nScreen Name = @" + str(screen_name) + " from " + str(
                location)
            print(write_location)
            results["user"] = str(user)
            results["screen_name"] = str(screen_name)
            results["location"] = str(location)
            results["write_location"] = str(write_location)
        except Exception as Error:
            print("User Name Error: \n" + str(Error))
            results["user"] = "User Not Available"
            results["screen_name"] = "Screen Name Not Available"
            results["location"] = "Location Not Available"
            results["write_location"] = "Location Not Available"

        try:
            text = tweet['text']
            print("------------------------")
            write_text = "Text = " + str(text)
            print(write_text)
            print("------------------------")
            results["text"] = str(text)
            results["write_text"] = str(write_text)
        except Exception as Error:
            print("User Name Error: \n" + str(Error))
            text = ""
            results["text"] = "Text Not Available"
            results["write_text"] = "Text Not Available"

        try:
            rt_data = tweet['retweeted_status']

            try:
                ext_text = rt_data['extended_tweet']
                full_text = ext_text['full_text']
                write_fulltext = "Full Text = " + str(full_text) + "\n"
                print(write_fulltext)
                results["full_text"] = str(full_text)
                results["write_fulltext"] = str(write_fulltext)
            except Exception as Error:
                print("Extended Text Error: " + str(Error))
                full_text = ""
                results["full_text"] = "Full Text Not Available"
                results["write_fulltext"] = "Full Text Not Available"

            try:
                try:
                    entities = rt_data['entities']
                    url_data = entities['urls']
                    url_list = url_data[0]
                    url = url_list['url']
                    write_url = "URL = " + str(url)
                    print(write_url)
                    results["url"] = str(url)
                    results["write_url"] = str(write_url)
                except Exception as Error:
                    print("Url data retrieving Error :" + str(Error))
                    entities = rt_data['entities']
                    url_data = entities['urls']
                    url = url_data['url']
                    write_url = "URL = " + str(url)
                    print(write_url)
                    results["url"] = str(url)
                    results["write_url"] = str(write_url)

            except Exception as Error:
                print("URL Error: " + str(Error))
                results["url"] = "Url Not Available"
                results["write_url"] = "Url Not Available"

            try:
                textchecker(full_text, text)
            except Exception as Error:
                print("Full Text Check Error is : " + str(Error))

        except Exception as Error:
            print("Re-tweet Error: " + str(Error))
            results["url"] = "Url Not Available"
            results["write_url"] = "Url Not Available"
            results["full_text"] = "Full Text Not Available"
            results["write_fulltext"] = "Full Text Not Available"

        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

        # print("Printing Results" + str(results))

    except Exception as Error:
        print("Error on Tweet Data is = " + str(Error))

    return results
