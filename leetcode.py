class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        val = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i
                val = nums[i - 1]
                break
        if val == None:
            nums.sort()
            return
        min_after = min(filter(lambda x: x > val, nums[index:]))
        
        min_index = len(nums) - nums[::-1].index(min_after) - 1
        nums[index - 1], nums[min_index] = nums[min_index], nums[index - 1]
        nums[index:] = sorted(nums[index:])


testcases = [
    # [1,2,3],
    [5,4,7,5,3,2]
]
sol = Solution()
for i in testcases:
    print(i, end=' ')
    sol.nextPermutation(i)
    print(i)