class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-2] *(amount+1)
        def dp(n):
            if n <= -1:
                return -1
            if n == 0:
                return 0
            if memo[n] == -2:
                min_cnt = float("inf")
                for coin in coins:
                    cnt = dp(n-coin)
                    if cnt >= 0:
                        min_cnt = min(min_cnt, 1+cnt)
                memo[n] = min_cnt
            return memo[n]
        ans = dp(amount)
        return ans if ans != float("inf") else -1              

        