mem = {}

def fib(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return b

print(fib(4))