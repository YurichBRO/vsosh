def solve(nums):
    l = 0
    r = len(nums) - 1
    point = -1
    while l < r:
        m = (l + r) >> 1
        if nums[l] < nums[m]:
            l = m
        elif nums[r] > nums[m]:
            r = m 
        else:
            point = l
            break
    return nums[point + 1]

testcases = [
    [1, 2, 3, 4, 5],
    [4, 5, 1, 2, 3],
    [2, 3, 4, 5, 1]
]
for i in testcases:
    print(solve(i), i)