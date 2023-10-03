import json

# Load the JSON data from 'data.json'
with open('DataHinglish.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

# Your Hinglish_Preprocessing functions
from Hinglish_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words
from Hinglish_Preprocessing.stemming import stem_word

stemmed_dataset = []

# Process the intents
for intent in intents["intents"]:
    stemmed_patterns = [stem_word(pattern) for pattern in intent["patterns"]]
    intent["patterns"] = stemmed_patterns
    stemmed_dataset.append(intent)

# Print the stemmed dataset
for intent in stemmed_dataset:
    print("Tag:", intent["tag"])
    print("Stemmed Patterns:", intent["patterns"])
    print("Responses:", intent["responses"])
    print()
