def tokenization_of_words(text):
    # text = "success confess dies subclasses a the"
    # text = "Hello, I am Abhishek, This is an example for how to remove the stopwords."
    special_characters = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', ':', ';',
                              '<', '=', '>', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\t', ',', '.','?']
    for i in special_characters:
        text = text.replace(i, '')
    tokens = text.split()
    return tokens