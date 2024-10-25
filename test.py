class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def f(nums):
            if len(nums) == 1:
                return nums
            result = []
            for i in nums:
                print(i, f(nums - {i}))
                for j in f(nums - {i}):
                    perm = [i, *j]
                    result.append(perm)
            return result
            
        return f(set(nums))
    
print(Solution().permute([1,2,3]))

