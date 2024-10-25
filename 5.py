def solve(s):
    return set([''.join([j for j in i.lower() if j.isalpha()]) for i in s.split()])

print(solve("A, a b c, ghghgh"))
print(solve("Hello, world! Hello everyone."))