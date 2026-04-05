class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        right = 0
        while right < len(nums) - 1:
            if nums[right] < nums[right + 1] :
                right += 1
            else :
                ans = max(ans, right - left + 1)
                left = right + 1
                right += 1
        return max(ans, right - left + 1)            
                 
        