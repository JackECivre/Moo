

def save_line(line_no, col, worksheet, now_time, time, username, location, text, full_text, url):
    print("line_no_b: " + str(line_no))
    row = line_no
    tweet = (
        [now_time, time, username, location, text, full_text, url],)

    try:
        for now_time, time, username, location, text, full_text, url in tweet:
            try:
                worksheet.write_string(row, col, now_time)
            except Exception as Error:
                worksheet.write_string(row, col, "save_time Not Available")
                print(str(Error))

            try:
                worksheet.write_string(row, col + 1, str(time))
            except Exception as Error:
                worksheet.write(row, col, "Time Not Available")
                print(str(Error))

            try:
                worksheet.write_string(row, col + 3, str(username))
            except Exception as Error:
                worksheet.write_string(row, col, "Username Not Available")
                print(str(Error))

            try:
                worksheet.write_string(row, col + 4, str(location))
            except Exception as Error:
                worksheet.write_string(row, col, "Location Not Available")
                print(str(Error))

            try:
                worksheet.write_string(row, col + 5, str(text))
            except Exception as Error:
                worksheet.write_string(row, col, "Text Not Available")
                print(str(Error))

            if full_text is not None:
                try:
                    worksheet.write_string(row, col + 6, str(full_text))
                except Exception as Error:
                    worksheet.write_string(row, col, "Full Text Not Available")
                    print(str(Error))
            else:
                worksheet.write_string(row, col, "Full Text Not Available")

            try:
                worksheet.write_url(row, col + 7, str(url))
            except Exception as Error:
                worksheet.write_string(row, col, "URL Not Available")
                print(str(Error))

        print("\nData Saved to Excel\n")

    except Exception as Error:
        print("Excel Save Error: " + str(Error))

    return True
