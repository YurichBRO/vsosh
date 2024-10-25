from collections import defaultdict

def solve(l):
    result = defaultdict(list)
    for i in l:
        result[''.join(sorted(i))].append(i)
    return [result[i] for i in result]

print(solve(['tea', 'eat', 'pot']))