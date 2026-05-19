class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * (len(nums)) for i in range(len(nums))]
        def dp(ind,last):
            if ind >= len(nums):
                return 0 
            if memo[ind][last] == -1:  
                inc = 0 
                if last == -1 or nums[ind] > nums[last]:
                    inc = 1 + dp(ind+1, ind)  
                exc = dp(ind+1,last)
                memo[ind][last] = max(inc, exc)  
            return memo[ind][last]
        return dp(0,-1)            
        