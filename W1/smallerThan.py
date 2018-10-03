def smaller_than(n1, n2):
    diff = n1 / n2
    return n1 if (diff < 1) else n2 if (diff > 1) else None

# print(smaller_than(1.2,1.22))
# print(smaller_than(2,1))
# print(smaller_than(2,2))