import json

with open('data.json', 'r') as f:
    intents = json.load(f)
    

from English_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words
from English_Preprocessing.stemming import stemming
from English_Preprocessing.removalStopWords import removal_of_stop_words


all_words = []
tags = []
xy = []
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        print("******** Data before tokenization ********", "\n")
        print(pattern)
        w = tokenization_of_words(pattern)
        print("\n", "******** tokenization the words ********", "\n")
        print("Tokenized Words", w)
        w2 = removal_of_stop_words(w)
        print("\n","******** Removed the Stop words ********", "\n")
        print("Stopwords after Removed", w2)
        # print("**************************************** print the Stemming of words ************************************************" ,"\n\n")
        w3=stemming(w2)
        print("\n", "******** Stemming of words ********" ,"\n")
        print("Stemmed Words", w3)
        # add to our words list
        all_words.extend(w3)
        # add to xy pair
        xy.append((w3, tag))
        
        print('\n\n')




# stem and lower each word
ignore_words = ['?', '.', '!']
# all_words = [stem(w) for w in all_words if w not in ignore_words]
# remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "patterns" , '\n')
print(len(tags), "tags:", tags , '\n')
print(len(all_words), "unique stemmed words:", all_words , '\n')