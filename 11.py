from collections import defaultdict

def solve(l):
    names = defaultdict(int)
    for i in l:
        names[i[0]] = max(names[i[0]], i[1])
    return sorted(sorted(names.items(), key=lambda x: x[0]), key=lambda x: x[1])

print(solve([('alice', 28), ('alice', 30), ('bob', 25)]))