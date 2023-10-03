# Function: To remove stop words from the list of words
# from tokenization import tokenization_of_words
stop_words = {'did', "couldn't", 'it', 'some', 'him', 'do', "hadn't", 'the', 'had', 'when', 'wouldn', "hasn't", 'doesn', 'he', 'how', 'once', 'this', 'been', 'also', 'an', "it's", 'under', 'if', 'which', 'be', 's', "don't", 'further', 'until', 'every', "you'll", 'our', 'only', 'move', 'didn', 'again', 'hasn', 'am', 'isn', 'are', "you'd", 'everything', 'because', 't', 'does', 'were', 'yours', 're', 'with', 'ourselves', 'she', 'where', 'such', 'hers', 'being', 'out', 'ma', 'i', 'too', 'ain', 'from', 'or', 'made', 'and', 'above', 'no', 'shan', 'll', 'mightn', "should've", 'If', 'a', 'other', 'himself', 'why', 'don', "wasn't", 'have', 'here', 'can', 'doing', 'up', 'yourselves', 'as', 'off', "aren't", 'mustn', 'itself', 'yourself', 'its', 'won', 'my', 'aren', 'at', 'that', 'than', 'shouldn', 'His', 'bhagat', 'o', 'm', "weren't", 'whom', 'y', 'couldn', 'weren', "mightn't", 'for', 'just', "you've", 'ours', 'those', 'between', 'through', 'is', "wouldn't", 'these', 'any', "won't", 've', 'has', "that'll", 'about', "doesn't", 'against', 'hadn', 'you', 'most', 'while', 'after', "she's", 'his', 'into', 'who', 'on', 'during', 'will', 'they', 'by', 'below', 'in', "shan't", 'each', 'so', 'having', 'theirs', 'more', 'nor', 'few', 'we', 'then', "didn't", 'down', 'wasn', 'them', 'was', "mustn't", 'very', 'herself', 'not', "isn't", 'nikunj', 'over', 'what', 'should', "haven't", 'themselves', 'myself', 'both', 'of', "shouldn't", 'someone', 'needn', "you're", 'their', 'now', "needn't", 'but', 'there', 'all', 'haven', 'her', 'same', 'me', 'your', 'before', 'to', 'd', 'own'}

# print(len(stop_words))
# print(stop_words)


def removal_of_stop_words(words):
    all_words = []
    for w in words:
        if w.lower() not in stop_words:
            all_words.append(w)

    return all_words
