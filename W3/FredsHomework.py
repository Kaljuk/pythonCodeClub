
def isNumber():
    pass

def solve_freds_homework(equation):
    equation = equation.split("=")
    # Left
    left = equation[0].split(" ")
    # Right
    right= [0] if (len(equation) <= 1) else equation[1].split(" ")

    ## Remove spaces
    left = list(filter(lambda x: x!='', left))
    right= list(filter(lambda x: x!='', right))
    
    ## Bring - symbol slave into the master
    newLeft = []
    passNext = False
    for i in range(len(left)):
        if (passNext):
            passNext = False
            continue
        if (left[i] == '-' and i < len(left)):
            passNext = True
            newLeft.append(left[i]+left[i+1])

    ## Count x and y-s
    

    print(left, right)


e = "50 = x - y"
solve_freds_homework(e)
e = "x - y"
solve_freds_homework(e)
# print(solve_freds_homework(e))