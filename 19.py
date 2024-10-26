def solve(n, m):
    result = []
    for i in range(n, m + 1, n):
        result.append(i)
    return (result, sum(result))

print(*solve(3, 20))