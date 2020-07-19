

def save_on_text_file(filename_text, tweet_desired_data, now_time, tweet):

    with open(filename_text, 'a', encoding="utf-16") as tf:
        tf.write("\n--------------------------------------- TWEET -----------------------------------------\n")
        tf.write("Tweet registered on file at " + str(now_time) + "\n")
        try:
            try:
                tf.write(tweet_desired_data["write_time"] + "\n")
            except Exception as Error:
                tf.write("Time error = \n" + str(Error) + "\n")

            try:
                tf.write(tweet_desired_data["write_location"] + "\n")
            except Exception as Error:
                tf.write("Location error = \n" + str(Error) + "\n")

            try:
                tf.write(tweet_desired_data["write_url"] + "\n")
            except Exception as Error:
                print("URL error = \n" + str(Error) + "\n")
                tf.write("URL is not Available" + "\n")

            try:
                tf.write(tweet_desired_data["write_text"] + "\n\n")
            except Exception as Error:
                tf.write("Text error = \n" + str(Error) + "\n")

            try:
                tf.write(tweet_desired_data["write_fulltext"] + "\n")
            except Exception as Error:
                print("Full Text Error = \n" + str(Error) + "\n")
                tf.write("Full Text is not Available" + "\n")

            tf.write(
                "-------------------------------------END OF Summary---------------------------------------\n\n")
            tf.write("--------------------------------------Tweet Data----------------------------------------\n\n")
            tf.write(str(tweet) + "\n\n")
            tf.write(
                "-------------------------------------END OF TWEET---------------------------------------\n\n\n")
            return True

        except Exception as Error:
            tf.write(str(Error))
            tf.write("Tweet error detected. \n" + tweet + "\n")

        print("\nData Saved to File\n")
        return True
