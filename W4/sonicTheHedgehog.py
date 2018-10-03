def sonic_how_many_rings_did_you_get(input_string):
    sumThis = [(1 if (c in "qQeRoOpPadDgb069") else 2 if(c in 'B8') else 0) for c in input_string]
    return sum(sumThis)