import json

with open('data.json', 'r') as f:
    intents = json.load(f)

from Preprocessing.tokenization import tokenization_of_words

from Preprocessing.removalStopWords import removal_of_stop_words

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
        w = tokenization_of_words(pattern)
        print("Tokenized Words", w)
        w2 = removal_of_stop_words(w)
        print("Stopwords Removed", w2)
        # add to our words list
        all_words.extend(w2)
        # add to xy pair
        xy.append((w2, tag))




# stem and lower each word
ignore_words = ['?', '.', '!']
# all_words = [stem(w) for w in all_words if w not in ignore_words]
# remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "unique stemmed words:", all_words)