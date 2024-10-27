def solve(n, m, v, links):
    matrix = [[0 for i in range(n)] for i in range(n)]
    for link in links:
        matrix[link[0] - 1][link[1] - 1] = 1
        matrix[link[1] - 1][link[0] - 1] = 1
    inf = float('inf')
    dist = [inf for i in range(n)]
    v -= 1
    dist[v] = 0
    vertex = v
    min_dist = 0
    selected = [False for i in range(n)]
    while min_dist < inf:
        selected[vertex] = True
        for i in range(len(matrix)):
            new_dist = dist[vertex] + matrix[vertex][i]
            if new_dist < dist[i] and matrix[vertex][i] != 0:
                dist[i] = new_dist
        min_dist = inf
        for i in range(len(matrix)):
            if not selected[i] and dist[i] < min_dist:
                min_dist = dist[i]
                vertex = i
    dist = [i for i in enumerate(dist) if i[1] != inf]
    dist.sort(key=lambda x: x[1])
    return [i[0] + 1 for i in dist]


print(solve(3, 2, 1, [[1, 2], [2, 3]]))
print(solve(4, 4, 1, [[1, 2], [2, 3], [3, 4], [4, 1]]))