def solve(n):
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

print(solve(120))