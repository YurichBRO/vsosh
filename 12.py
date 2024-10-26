def solve1(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def solve2(n):
    if n == 1:
        return 1
    return n * solve2(n-1)

print(solve1(7), solve2(7))