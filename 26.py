def solve(lst, n):
    l = 0
    r = len(lst) - 1
    index = None
    while l <= r:
        m = (l + r) >> 1
        if lst[m] < n:
            l = m + 1
        elif lst[m] > n:
            r = m - 1
        else:
            index = m
            break
    else:
        index = l
    lst.insert(index, n)

l = [1, 2, 3, 3, 5, 5]
solve(l, 4)
print(l)