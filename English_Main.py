import json
import random
from English_Preprocessing.tokenization import tokenize_without_numbers as tokenization_of_words
from English_Preprocessing.stemming import stemming
from English_Preprocessing.removalStopWords import removal_of_stop_words

# Load your intents data from the JSON file
with open('data.json', 'r') as f:
    intents = json.load(f)

# Preprocess user input
def preprocess_input(user_input):
    words = tokenization_of_words(user_input)
    words = removal_of_stop_words(words)
    words = stemming(words)
    return words

# Function to calculate similarity between two lists of words
def get_similarity_score(input_words, pattern_words):
    if not input_words or not pattern_words:
        return 0.0  # Return 0 if either list is empty

    common_words = set(input_words) & set(pattern_words)
    similarity = len(common_words) / max(len(input_words), len(pattern_words))
    return similarity

# Function to get a response
def get_response(user_input):
    user_input = preprocess_input(user_input)

    best_match_intent = None
    best_match_score = 0

    # Iterate through the intents and patterns
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_words = preprocess_input(pattern)
            similarity_score = get_similarity_score(user_input, pattern_words)
            if similarity_score > best_match_score:
                best_match_score = similarity_score
                best_match_intent = intent

    if best_match_intent and best_match_score >= 0.7:  # Adjust the similarity threshold as needed
        responses = best_match_intent['responses']
        return random.choice(responses)  # Select a random response from the available responses

    return "I'm sorry, I don't understand that."

# Interactive loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
