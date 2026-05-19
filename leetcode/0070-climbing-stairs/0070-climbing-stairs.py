class Solution:
    def climbStairs(self, n: int) -> int:
        me = defaultdict(int)
        def memo(n):
            if n == 1:
                return n
            if n == 2:
                return 2    
            if n not in me:
                me[n] = memo(n-1) + memo(n-2)
            return me[n]
        return memo(n)             