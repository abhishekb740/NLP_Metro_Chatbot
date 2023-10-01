def tokenization_of_words():
    text = "success confess dies subclasses"
    special_characters = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';',
                              '<', '=', '>', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\t', ',', '.','?']
    for i in special_characters:
        text = text.replace(i, '')
    tokens = text.split()
    return tokens