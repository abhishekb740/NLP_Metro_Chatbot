import json

with open('data.json', 'r') as f:
    intents = json.load(f)


from English_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words
from English_Preprocessing.stemming import stemming
from English_Preprocessing.removalStopWords import removal_of_stop_words


all_words = []
tags = []
xy = []

count = 0
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        print("************* Data Processing", count, "**************\n")
        count = count+1
        # tokenize each word in the sentence
        print("Data : ", pattern, "\n")
        w = tokenization_of_words(pattern)
        print("Data After Tokenization", w, "\n")
        w2 = removal_of_stop_words(w)
        print("Data After Removal of Stopwords", w2, "\n")
        w3 = stemming(w2)
        print("Data After stemming", w3, "\n")
        # create our training data
        join_words = ' '.join(w3)
        print("Final Data : ", join_words, "\n\n\n\n\n")
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

print(len(xy), "patterns", '\n')
print(len(tags), "tags:", tags, '\n')
print(len(all_words), "unique stemmed words:", all_words, '\n')
