class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        for i in range(len(nums)):
            nums[i] = temp.index(nums[i])
        return nums    
        
