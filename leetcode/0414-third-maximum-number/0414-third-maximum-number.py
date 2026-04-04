class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = set(nums)
        temp = list(temp)
        temp.sort()
        if len(temp) < 3:
            return temp[-1]
        else:
            return temp[-3]    
        