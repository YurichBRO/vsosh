def solve(n, m, links):
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in links:
        matrix[i[0] - 1][i[1] - 1] = 1
        matrix[i[1] - 1][i[0] - 1] = 1
    def walk(i, seen=set()):
        if len(seen) == len(matrix):
            return True
        for index, value in enumerate(matrix[i]):
            if not value:
                continue
            if index in seen:
                continue
            if walk(index, seen | {index}):
                return True
        return False
    res = walk(0, set([0]))
    print("YES" if res else "NO")

solve(3, 2, [[1, 2], [3, 2]])
solve(3, 1, [[1, 3]])