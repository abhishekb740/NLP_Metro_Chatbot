from tokenization import tokenization_of_words

vowels = set(['a', 'e', 'i', 'o', 'u'])

step1a_set = [
    ("sses", "ss"),  # SSES -> SS
    ("ies", "i"),  # IES  -> I
    ("ss", "ss"),
    ("s", ""),  # S    ->
]

# step1b_set = [
#      ("")
# ]



def stemming():
    all_words = tokenization_of_words()
    print((all_words))
    # all_words = [stem(w) for w in all_words if w not in ignore_words]
    stemmed_word = []
    for w in all_words:
            for rules in step1a_set:
                suffix, replace = rules
                if w.endswith(suffix):
                    w = w[:-len(suffix)] + replace
            stemmed_word.append(w)
    return stemmed_word


new_words = stemming()
print(new_words)
