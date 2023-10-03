import re

# Stemming function using the given regex pattern
def stem_word(word):
    return re.sub(r'(.{2,}?)([aeiougyn]+$)', r'\1', word)
