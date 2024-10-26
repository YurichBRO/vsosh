def is_palindrome(n):
    n = str(n)
    for i in range(len(n) // 2):
        if n[i] != n[-i-1]:
            return False
    return True

def solve(n):
    buffer = [True for _ in range(n - 1)]
    for i in range(2, int(n ** .5) + 1):
        for j in range(2*i - 2, n - 1, i):
            buffer[j] = False
    result = []
    for i in range(n - 1):
        if not buffer[i]:
            continue
        if is_palindrome(i + 2):
            result.append(i + 2)

from time import time
start = time()
solve(1000000)
end = time()
print(end - start)