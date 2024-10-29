def solve(a1, a2, m, n, x):
    diff = float('inf')
    l = 0
    r = n - 1
    while(l < m and r >= 0):
        if abs(a1[l] + a2[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(a1[1] + a2[r] - x)
        if a1[l] + a2[r] > x:
            r -= 1
        else:
            l += 1
    print(f"the closest pair is [{a1[res_l]}, {a2[res_r]}]")
a1 = [1, 4, 5, 7]
a2 = [2, 5, 6, 8]
m = len(a1)
n = len(a2)
x = 14
solve(a1, a2, m, n, x)