

def textchecker(full_text, text):
    fulltext_list= full_text.split()
    # print("Full Text List is : " + str(fulltext_list))
    text_list = text.split()
    # print("Text List is : " + str(text_list))
    if text_list[2] == fulltext_list[0] or text_list[3] == fulltext_list[1]:

        True
        print("Text to Full Text Check : Success")
    else:
        full_text = None
        # print(full_text)
        print("Full text is not same with text")

    return True