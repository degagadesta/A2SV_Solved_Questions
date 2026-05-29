class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float("inf")
        for num in nums:
            tot = 0
            while num > 0:
                tot += (num % 10)
                num //= 10
            min_num = min(min_num, tot)
        return min_num        
        