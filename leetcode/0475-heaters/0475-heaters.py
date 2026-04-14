class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def helper(r):
            cnt = 0 
            j = 0
            for i in houses:
                while j < len(heaters):
                    if abs(i - heaters[j]) <= r:
                        cnt += 1
                        break
                    j += 1    
            return cnt == len(houses)   
        left = -1
        right = 10 ** 9
        while left + 1 < right :
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid
        return right                          

        