import json

# Load the JSON data from 'data.json'
with open('DataHinglish.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

# Your Hinglish_Preprocessing functions
from Hinglish_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words
from Hinglish_Preprocessing.stemming import stem_word

all_words = []
tags = []
xy = []
# Process the intents
for intent in intents["intents"]:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenization_of_words(pattern)
        print("**************************************** print the tokenization of words ************************************************", "\n\n")
        print("Tokenized Words", w)
        # print("Tokenized Hinglish",w)
        stemmed_words = []
        for word in w:
            w1 = stem_word(word)
            stemmed_words.append(w1)
        print("**************************************** print the Stemming of words ************************************************" ,"\n\n")
        print("Stemmed Words", stemmed_words)

# Print the stemmed dataset
# for intent in stemmed_dataset:
#     print("Tag:", intent["tag"])
#     print("Stemmed Patterns:", intent["patterns"])
#     print("Responses:", intent["responses"])
#     print()
