# def tokenization_of_words():
#     text = "success confess dies subclasses a the"
#     # text = "Hello, I am Abhishek, This is an example for how to remove the stopwords."
#     special_characters = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';',
#                               '<', '=', '>', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\t', ',', '.','?']
#     for i in special_characters:
#         text = text.replace(i, '')
#     tokens = text.split()
#     return tokens


# def tokenize(text):

    
#     tokens = []
#     current_token = ""

#     for char in text:
#         if char.isalnum() or char == "'":
#             current_token += char
#         else:
#             if current_token:
#                 tokens.append(current_token)
#                 current_token = ""
#             if char.strip():
#                 tokens.append(char)

#     if current_token:
#         tokens.append(current_token)
#     print(tokens)
#     return tokens

# # Example usage
# # text = "Tokenization is important for NLP!"
# # tokens = tokenize(text)



# import json

# # Load the JSON data
# with open('intents.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# # Access the intents
# intents = data['intents']

# # Example: Print all patterns for each intent
# for intent in intents:
#     # tokenize(intent['tag'])
#     print(f"Intent: {intent['tag']}")
#     print("Patterns:")
#     for pattern in intent['patterns']:
#         # print(pattern)
#         tokenize(pattern)
#     print()



# # import re

# # def tokenize_with_regex(text):
# #     # Define a regex pattern for tokenization
# #     pattern = r'\w+|[^\w\s]'

# #     # Use the findall() function to extract tokens
# #     tokens = re.findall(pattern, text)
# #     return tokens

# # # Example usage
# # text = "Tokeniz6ation using regex is awesome!"
# # tokens = tokenize_with_regex(text)
# # print(tokens)


import re

def tokenize_without_numbers(text):
    pattern = r'\b[a-zA-Z]+\b'  # Matches words containing only letters

    # Use findall() to get all matching tokens
    tokens = re.findall(pattern, text)
    newTokens = []
    for token in tokens:
        newTokens.append(token.lower())
    return newTokens

# text = "Tokeniz6ation USSing REGEX is awesome!"

# print(tokenize_without_numbers(text))
