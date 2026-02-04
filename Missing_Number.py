class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s= sum(nums)
        cnt=0
        for i in range(len(nums)+1):
            cnt += i
        return cnt-s    
       
        
