import random

def D10():
    D10 = random.randint(1, 10)
    if D10 <= 9 and D10 >= 3:
        int(D10)
    elif D10 <= 2:
        int(D10)
    else:
        int(D10)

    return D10

def D6():
    D6 = random.randint(1, 6)
    if D6 == 3 or D6 == 2:
        int(D6)

    elif D6 == 1:
        int(D6)
    else:
        int(D6)

    return D6