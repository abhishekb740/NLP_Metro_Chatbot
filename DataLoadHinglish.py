import json

# Load the JSON data from 'data.json'
with open('DataHinglish.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

# Your Hinglish_Preprocessing functions
from Hinglish_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words

from Hinglish_Preprocessing.stemming import stem_word as stemming

from Hinglish_Preprocessing.removalStopWords import Hinglish_stop_words as HindiStopWords

all_stemWords = []
tags = []
xy = []

# Process the intents
for intent in intents["intents"]:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        print("******** Data before tokenization ********", "\n")
        print(pattern)
        w = tokenization_of_words(pattern)
        print("\n", "******** tokenization the words ********", "\n")
        print("Tokenized Words", w)
        
        w1 = HindiStopWords(w)
        print("\n","******** Removed the Stop words ********", "\n")
        print("Stopwords after Removed", w1)
        
        stemmed_words = []
        for word in w1:
            w2 = stemming(word)
            stemmed_words.append(w2)
        print("\n", "******** Stemming of words ********" ,"\n")
        print("Stemmed Words", stemmed_words , "\n")
        
        xy.extend((tag , stemmed_words))



print(len(xy), "patterns" , xy , '\n')
print(len(tags), "tags:", tags , '\n')
print(len(stemmed_words), "unique stemmed words:", stemmed_words , '\n')
