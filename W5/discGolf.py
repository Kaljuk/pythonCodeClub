

def order_discgolfers(scores):
    scores.sort(ley=lambda x: x)


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

order_discgolfers(scores)