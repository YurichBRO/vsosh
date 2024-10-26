def solve(n):
    if n < 2:
        return False
    if not (n & 1):
        return False
    for i in range(3, int(n ** .5) + 1, 2):
        if not (n % i):
            return False
    return True

print(solve(3), solve(4), solve(17), solve(18))