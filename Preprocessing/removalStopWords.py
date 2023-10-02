import nltk
from nltk.corpus import stopwords
# from tokenization import tokenization_of_words
stop_words = set(stopwords.words('english'))


def removal_of_stop_words(words):
    all_words = []
    for w in words:
        if w.lower() not in stop_words:
            all_words.append(w)
    
    return all_words



