class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(n):
            cnt = 1
            s = 0
            left = 0
            for i in range(len(position)):
                if position[i] - position[left] >= n:
                    cnt += 1
                    left = i
            return cnt >= m
        left = 0 
        right = position[-1] 
        while left + 1 < right :
            mid = (left + right ) // 2    
            if helper(mid) :
                left = mid
            else:
                right = mid
        return left            


        