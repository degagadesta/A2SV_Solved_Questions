class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = abs(0 - (sum(nums) - nums[0]))
        left = [0] * len(nums)
        for i in range(1, len(nums)):
            left[i] += left[i-1] + nums[i-1]
            ans[i] = abs(left[i] - (sum(nums) - nums[i] - left[i]))
        return ans    
