def coolest_word(words):
    return None if (words == []) else max(words, key=lambda word: None if (word == None) else len(set(word)) )