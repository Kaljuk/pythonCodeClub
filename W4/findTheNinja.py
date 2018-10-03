def identify_ninja(ninja, people):
    sortedPeople = [''.join(sorted(p)) for p in people]
    hashedPeople = [hash(p) for p in sortedPeople]

    sortedNinja  = ''.join(sorted(ninja))
    hashedNinja  = hash(sortedNinja)
    
    potentialNames = []
    for h in range(len(hashedPeople)):
        if (hashedPeople[h] == hashedNinja):
            potentialNames.append(people[h])
    return potentialNames





print(identify_ninja('obb', ['bob', 'richard', 'bbo', 'bob']))
# print(identify_ninja('obb', ['bobs', 'richard']))
