def algo(matrix):
    inf = float('inf')
    min_dist = 0
    selected = [0 for i in range(len(matrix))]
    dist = [inf for i in range(len(matrix))]
    start = 0
    dist[start] = 0
    V = start
    letters = [chr(ord('A') + i) for i in range(len(matrix))]

    while min_dist < inf:
        selected[V] = True
        for i in range(len(matrix)):
            new_dist = dist[V] + matrix[V][i]
            if new_dist < dist[i] and matrix[V][i] != 0:
                dist[i] = new_dist
        min_dist = inf
        for i in range(len(matrix)):
            if not selected[i] and dist[i] < min_dist:
                min_dist = dist[i]
                V = i
    
    V = len(matrix) - 1
    print(dist[V])
    print(letters[V])
    while V != start:
        for i in range(len(matrix)):
            if i != V and dist[i] + matrix[i][V] == dist[V]:
                V = i
                break
        print(letters[V])

matrix = [
#    A B C D E F
    [0,2,4,0,0,0],#A
    [2,0,9,7,0,0],#B
    [4,9,0,8,1,0],#C
    [0,7,8,0,3,1],#D
    [0,0,1,3,0,2],#E
    [0,0,0,1,2,0],#F
]

algo(matrix)