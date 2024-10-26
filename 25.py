def sum_of_digits(n):
    return sum(int(i) for i in str(n))

def mul_of_digits(n):
    digits = (int(i) for i in str(n))
    result = 1
    for i in digits:
        result *= i

def solve(n):
    if n % sum_of_digits(n):
        return False
    if n % mul_of_digits(n):
        return False
    return True