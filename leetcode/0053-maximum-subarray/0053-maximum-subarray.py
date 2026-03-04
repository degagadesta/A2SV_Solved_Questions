class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = nums[0]
        for i in range(1, len(nums) ):
            cur  = max(nums[i], cur + nums[i])
            ans = max(ans, cur)

        return ans    
        