class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = len(nums) - 1
        read = 0
        while read <= right :
            if nums[read] == 0:
                nums[left] , nums[read] = nums[read], nums[left]
                left += 1
                read += 1
            elif nums[read] == 2:
                nums[right], nums[read] = nums[read] , nums[right] 
                right -= 1
            else:
                read += 1    
               

        