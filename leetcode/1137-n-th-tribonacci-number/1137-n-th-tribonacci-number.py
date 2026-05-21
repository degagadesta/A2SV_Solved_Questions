class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1] * (n+1)
        def dp(n):
            if n == 0:
                return 0
            if n <= 2:
                return 1
            if memo[n] == -1:
                memo[n] = dp(n-1) + dp(n-2)+ dp(n-3)        

            return memo[n]
        return dp(n)                