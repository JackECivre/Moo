import csv
import os.path


def create_excel_file(filename_excel, tweet_desired_data, now_time):

    try:
        file_exists = os.path.isfile(filename_excel)

        with open(filename_excel, 'a', newline='', encoding="utf-16") as csv_file:
            fieldnames = ['Data Collection Time', 'Tweet Time', 'Tweet User Name', 'Tweet Location', 'Tweet Text',
                          'Tweet Full Text', 'URL', 'Language']

            time = tweet_desired_data["time"]
            username = tweet_desired_data["user"]
            location = tweet_desired_data["location"]
            text = tweet_desired_data["text"]
            full_text = tweet_desired_data["full_text"]
            url = tweet_desired_data["url"]
            language = tweet_desired_data["language"]
            # print(language)

            writer = csv.DictWriter(csv_file, delimiter=",", fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({'Data Collection Time': now_time,
                             'Tweet Time': time,
                             'Tweet User Name': username,
                             'Tweet Location': location,
                             'Tweet Text': text,
                             'Tweet Full Text': full_text,
                             'URL': url,
                             'Language': language})
            print("Excel Data Saved.")
    except Exception as Error:
        print("Excel File Save Error : " + str(Error))

    return True
