class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        temp = [str(nums[i]) for i in range(len(nums))]
        temp.sort(key = lambda item : item *20, reverse = True)
        if temp[0] == "0":
          return "0"
  
        return "".join(temp)    
        
