from collections import defaultdict
from time import time

def solve(n, m, links):
    if n < 3:
        print(0)
        return
    start = time()
    links = {(i[0] - 1, i[1] - 1) for i in links}
    nodes = [set() for i in range(n)]
    for i in links:
        i = list(i)
        if i[1] < i[0]:
            i = [i[1], i[0]]
        nodes[i[0]].add(i[1])
        nodes[i[1]].add(i[0])
    c = 0
    print(nodes)
    def walk(i, prev, prevprev=None):
        nonlocal c
        if prevprev > i:
            link = (i, prevprev)
        else:
            link = (prevprev, i)
        if link in links:
            c += 1
        for j in nodes[i]:
            print(i, j, nodes[i])
            if i in nodes[j]:
                nodes[j].remove(i)
        for j in nodes[i]:
            walk(j, i, prev)
    walk(0, -1, -1)
    print(c)

from random import randint

def generate(n, m):
    start = time()
    links = set()
    for i in range(m):
        link = (randint(1, n), randint(1, n))
        while link in links or link[0] == link[1]:
            link = (randint(1, n), randint(1, n))
        links.add(link)
    print("generate", time() - start)
    print(links)
    return (n, m, list(links))


a = generate(4, 5)

solve(4, 5, [[2,4], [3,4], [4,1], [2,3], [1,3]])