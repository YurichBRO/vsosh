def solve(n, m, links):
    nodes = [[] for _ in range(n)]
    for i in links:
        nodes[i[0] - 1].append(i[1] - 1)
        nodes[i[1] - 1].append(i[0] - 1)
    print(nodes)
    
    visited = set()
    def walk(i, prev):
        print(f'visited: {visited}; i: {i}; prev: {prev}')
        if i in visited and i != prev:
            return False
        visited.add(i)
        for j in nodes[i]:
            if j == prev:
                continue
            if not walk(j, i):
                return False
        return True
    
    print("YES" if walk(0, -1) else "NO")

solve(4, 4, [[1, 2], [1, 3], [2, 4]])