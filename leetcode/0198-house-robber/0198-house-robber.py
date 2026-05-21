class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def dp(n):
            if n <= 1:
                return nums[n]
            if n == 2:
                if n-2 not in memo:
                    memo[n-2] = dp(n-2)
                return nums[n] + memo[n-2]
            if n-2 not in memo:
                    memo[n-2] = dp(n-2)
            if n-3 not in memo:
                memo[n-3] = dp(n-3)        
            return nums[n] + max(memo[n-2],memo[n-3])
        return max(dp(len(nums)-1),dp(len(nums)-2))    

        