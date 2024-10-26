def NOD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def NOK(a, b):
    return a * b // NOD(a, b)

print(NOK(NOK(int(input()), int(input())), int(input())))