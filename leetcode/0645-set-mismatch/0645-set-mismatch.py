class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        for i in nums:
            ind = abs(i) - 1
            if nums[ind] < 0:
                res[0] = abs(i)
            else:    
                nums[ind] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res[1] = i+1
        return res                


        