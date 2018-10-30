# Teeing order on all subsequent holes is determined by the scores on the previous hole, with the lowest score throwing first, and so on. If the previous hole was a tie, the scores are to be counted back until the order is resolved.


def order_discgolfers(rounds):
    newOrder = []
    for round in list(reversed(rounds)):
        m = min(round.keys(), key=lambda x: round[x])
        print m
        
        for p in round:
            print(p, round[p])

        if (len(newOrder) >= len(round)): break
    
    return newOrder
    

scores = [{
    'bob': 3,
    'patric': 2,
    'squidward': 4,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 2,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}]

print(order_discgolfers(scores))
print(['squidward', 'patric', 'bob'])