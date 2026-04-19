class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0  or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            t = abs(nums[i])
            if t > n:
                continue
            if nums[t - 1] > 0:
                nums[t-1] *= -1
        for i in range(n):
            if nums[i] >= 0:
                return i + 1        
        return n + 1        



        