def solve(n):
    buffer = [i & 1 for i in range(n - 1)]
    for i in range(3, int(n ** .5) + 1, 2):
        for j in range(i * i, n, 2 * i):
            buffer[j - 2] = 0
    result = []
    for i in range(len(buffer) - 2):
        if buffer[i] and buffer[i + 2]:
            result.append((i + 2, i + 4))
    return result

print(solve(1000))