class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(md):
            cnt = 0
            for i in candies:
                cnt += (i // md)
            return cnt >= k    
        left = 0
        right = sum(candies) // k + 1
        while left + 1 < right :
            mid = (left + right) // 2
            if helper(mid):
                left = mid
            else:
                right = mid
        return left            

        