from collections import defaultdict

def solve(s):
    result = defaultdict(int)
    for i in s:
        result[i] += 1
    return (dict(result), ''.join(str(result[i]) for i in s))

print(solve("hello"))