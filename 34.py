def p(m):
    for i in m:
        for j in i:
            print(j, end=' ')
        print()
    print()

def solve(n, m, links):
    selected = [False for i in range(n)]
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in links:
        matrix[i[0] - 1][i[1] - 1] = 1
        matrix[i[1] - 1][i[0] - 1] = 1
    def walk(i, prev):
        for j in range(n):
            if not matrix[i][j]:
                continue
            if j == prev:
                continue
            if selected[j]:
                matrix[i][j] = 0
                matrix[j][i] = 0
            else:
                selected[j] = True
                walk(j, i)
    selected[0] = True
    walk(0, -1)

solve(4, 4, [[1, 2], [2, 3], [3, 4], [4, 1]])