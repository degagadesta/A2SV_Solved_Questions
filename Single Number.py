class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        res=nums[-1]
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                res=nums[i]
                break
            else:
                i+=2   
        return res         
            
        
