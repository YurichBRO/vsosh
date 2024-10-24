def search(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) >> 1
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return l

print(search([1, 2, 2, 2, 2, 2, 2, 3, 4, 5], 3))
print(search([1, 2, 2, 2, 2, 2, 2, 3, 4, 5], 6))