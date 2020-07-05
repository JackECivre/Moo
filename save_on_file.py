import datetime


def save_on_file(fetched_tweets_filename, write_time, write_location, write_url, write_text, write_fulltext, tweet):
    with open(fetched_tweets_filename, 'a', encoding="utf-8") as tf:
        tf.write("\n--------------------------------------- TWEET -----------------------------------------\n")
        tf.write("Tweet registered on file at " + str(datetime.datetime.now()) + "\n")
        try:
            try:
                tf.write(write_time + "\n")

            except Exception as Error:
                tf.write("Time error = \n" + str(Error) + "\n")


            try:
                tf.write(write_location + "\n")

            except Exception as Error:
                tf.write("Location error = \n" + str(Error) + "\n")


            try:
                tf.write(write_url + "\n")

            except Exception as Error:
                tf.write("URL error = \n" + str(Error) + "\n")


            try:
                tf.write(write_text + "\n\n")

            except Exception as Error:
                tf.write("Text error = \n" + str(Error) + "\n")


            try:
                tf.write(write_fulltext + "\n")

            except Exception as Error:
                tf.write("Full Text error = \n" + str(Error) + "\n\n")


        except Exception as Error:
            tf.write(str(Error))
            tf.write("Tweet error detected. \n" + tweet + "\n")

        tf.write("-------------------------------------END OF Summary---------------------------------------\n\n")
        tf.write("--------------------------------------Tweet Data----------------------------------------\n\n")
        tf.write(str(tweet) + "\n\n")
        tf.write("-------------------------------------END OF TWEET---------------------------------------\n\n\n")