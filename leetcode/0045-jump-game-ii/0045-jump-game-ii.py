class Solution:
    def jump(self, nums: List[int]) -> int:
        memo =[-1] * (len(nums))

        def dp(ind):
            if ind >= len(nums)-1:
                return 0
            if memo[ind] == -1:
                if nums[ind] == 0:
                    return float("inf") 
                min_m = float("inf")
                for i in range(1, nums[ind]+1):
                    min_m = min(min_m, dp(ind+i))

                memo[ind] = 1+min_m        
            return memo[ind]
        return dp(0)           
        