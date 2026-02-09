class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=dict()
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in temp:
                return [i,temp[complement]]
            temp[nums[i]]=i    

        
