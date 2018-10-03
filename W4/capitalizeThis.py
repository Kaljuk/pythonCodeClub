def capitalizing_this(input_string):
    capWord = []
    for w in input_string.split(' '):
        newWord = ''.join([(w[i].upper() if (i == 0) else w[i].lower()) for i in range(len(w))])
        capWord.append(newWord)
    return ' '.join(capWord)
#print(capitalizing_this('TERE MaAilM'))
