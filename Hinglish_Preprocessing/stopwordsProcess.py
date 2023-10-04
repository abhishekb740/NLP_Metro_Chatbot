content_list = []

with open('hinglishstopwords.txt', 'r') as file:  
    content_list = []
    for line in file.readlines():
        content_list.append(line.replace('\n', ''))

    # print(content_list)
    # print("\n\n")


def Hinglish_stop_words(words):
    all_words = []
    for w in words:
        if w.lower() not in content_list:
            all_words.append(w)

    return all_words



    # pattern = r'\b[a-zA-Z]+\b'  # Matches words containing only letters