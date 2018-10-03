

def coolest_word(words):
    uniqueCWords = [''.join(set(c)) for c in words]
    longestLength= 0
    longestWord  = None
    for i in range(len(uniqueCWords)):
        if (len(uniqueCWords[i]) > longestLength):
            longestLength = len(uniqueCWords[i])
            longestWord  = words[i]
    return longestWord

# returns decomposition
# print(coolest_word(['expectation', 'discomfort', 'half', 'decomposition']))
# print(coolest_word(['expectation', 'sadasbrtntyndiscomfort', 'half', 'decomposition']))