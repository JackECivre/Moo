import xlsxwriter


def create_excel_file(filename_excel, tweet_desired_data, now_time):

    with open(filename_excel, 'a', encoding="utf-8") as ef:
        ef.workbook = xlsxwriter.Workbook(filename_excel)
        worksheet = ef.workbook.add_worksheet()

        # Add an Excel formats.

        bold_format = ef.workbook.add_format({'bold': True})

        worksheet.write('A1', 'Data Collection Time', bold_format)
        worksheet.write('B1', 'Tweet Time', bold_format)
        worksheet.write('C1', 'Tweet User Name', bold_format)
        worksheet.write('D1', 'Tweet Location', bold_format)
        worksheet.write('E1', 'Tweet Text', bold_format)
        worksheet.write('F1', 'Tweet Full Text', bold_format)
        worksheet.write('G1', 'URL', bold_format)



        time = tweet_desired_data["time"]
        username = tweet_desired_data["user"]
        location = tweet_desired_data["location"]
        text = tweet_desired_data["text"]
        full_text = tweet_desired_data["full_text"]
        url = tweet_desired_data["url"]

        col = 0
        row = 0

        tweet = (
            [now_time, time, username, location, text, full_text, url],)
        line = [now_time, time, username, location, text, full_text, url]
        worksheet.write_column(row + 1, col, line)

        # try:
        #     for now_time, time, username, location, text, full_text, url in tweet:
        #         try:
        #
        #             worksheet.write_string(row, col, now_time)
        #         except Exception as Error:
        #             worksheet.write_string(row, col, "save_time Not Available")
        #             print(str(Error))
        #
        #         try:
        #             worksheet.write_string(row, col + 1, str(time))
        #         except Exception as Error:
        #             worksheet.write(row, col, "Time Not Available")
        #             print(str(Error))
        #
        #         try:
        #             worksheet.write_string(row, col + 2, str(username))
        #         except Exception as Error:
        #             worksheet.write_string(row, col, "Username Not Available")
        #             print(str(Error))
        #
        #         try:
        #             worksheet.write_string(row, col + 3, str(location))
        #         except Exception as Error:
        #             worksheet.write_string(row, col, "Location Not Available")
        #             print(str(Error))
        #
        #         try:
        #             worksheet.write_string(row, col + 4, str(text))
        #         except Exception as Error:
        #             worksheet.write_string(row, col, "Text Not Available")
        #             print(str(Error))
        #
        #         if full_text is not None:
        #             try:
        #                 worksheet.write_string(row, col + 5, str(full_text))
        #             except Exception as Error:
        #                 worksheet.write_string(row, col, "Full Text Not Available")
        #                 print(str(Error))
        #         else:
        #             worksheet.write_string(row, col, "Full Text Not Available")
        #
        #         try:
        #             worksheet.write_url(row, col + 6, str(url))
        #         except Exception as Error:
        #             worksheet.write_string(row, col, "URL Not Available")
        #             print(str(Error))
        #
        #     print("\nData Saved to Excel\n")
        #
        # except Exception as Error:
        #     print("Excel Save Error: " + str(Error))
        #
        # # ef.workbook.close()

        return True


