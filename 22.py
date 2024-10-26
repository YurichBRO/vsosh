def solve(l):
    max1 = -float('inf')
    max2 = -float('inf')
    for i in l:
        if i >= max1:
            max1, max2 = i, max1
    return max2

print(solve([1, 2, 3, 4, 5]))