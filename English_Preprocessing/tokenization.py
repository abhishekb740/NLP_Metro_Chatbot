import re

def tokenize_without_numbers(text):
    pattern = r'\b[a-zA-Z]+\b'  # Matches words containing only letters

    # Use findall() to get all matching tokens
    tokens = re.findall(pattern, text)
    newTokens = []
    for token in tokens:
        newTokens.append(token.lower())
    return newTokens

