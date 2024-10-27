from collections import defaultdict

def solve(n, m, links):
    nodes = [set() for i in range(n)]
    for i in links:
        nodes[i[0]].add(i[1])
        nodes[i[1]].add(i[0])
    sum = 0
    for i in nodes:
        sum += 