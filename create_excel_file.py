import csv


def create_excel_file(filename_excel, tweet_desired_data, now_time):
    try:
        with open(filename_excel, 'a', newline='', encoding="utf-16") as csvfile:
            fieldnames = ['Data Collection Time', 'Tweet Time', 'Tweet User Name', 'Tweet Location', 'Tweet Text',
                          'Tweet Full Text', 'URL']

            time = tweet_desired_data["time"]
            username = tweet_desired_data["user"]
            location = tweet_desired_data["location"]
            text = tweet_desired_data["text"]
            full_text = tweet_desired_data["full_text"]
            url = tweet_desired_data["url"]

            writer = csv.DictWriter(csvfile, delimiter=",", fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Data Collection Time': now_time,
                             'Tweet Time': time,
                             'Tweet User Name': username,
                             'Tweet Location': location,
                             'Tweet Text': text,
                             'Tweet Full Text': full_text,
                             'URL': url})
            print("Excel Data Saved.")
    except Exception as Error:
        print("Excel File Save Error : " + str(Error))

    return True
