def solve(n, links):
    mem = {}
    def walk(i):
        print(i)
        if i == -1:
            return 0
        if i in mem:
            return mem[i]
        res = walk(links[i] - 2) + 1
        mem[i] = res
    
    for i in range(len(links)):
        walk(i)
    max_dist = 0
    max_nodes = 0
    for i in mem:
        if mem[i] > max_dist:
            max_dist = mem[i]
            max_nodes = [i + 2]
        elif mem[i] == max_dist:
            max_nodes.append(i + 2)
    return (max_dist, len(max_nodes), max_nodes)
        

print(solve(3,[1,2]))