class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ans = float("-inf")
        nums.sort()
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i-1])

        return ans if len(nums) > 1 else 0           