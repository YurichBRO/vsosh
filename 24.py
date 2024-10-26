def factorize(n):
    if n < 2:
        return n
    
    factors = []
    while n & 1 == 0:
        factors.append(2)
        n >>= 1

    for i in range(3, int(n ** .5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 1:
        factors.append(n)

    return factors

def multiply(l):
    all_results = []
    for i in range(2 ** len(l) - 1):
        numbers = []
        index = 0
        while i:
            if i & 2:
                numbers.append(l[0])
            i >>= 1
            index += 1
        result = 1
        for i in numbers:
            result *= i
        all_results.append(result)
    return all_results

def solve(n):
    print(multiply(factorize(n)))
    return n == sum(multiply(factorize(n)))

def solveN(n):
    for i in range(1, n):
        if solve(n):
            yield n

print(*solveN(1000))