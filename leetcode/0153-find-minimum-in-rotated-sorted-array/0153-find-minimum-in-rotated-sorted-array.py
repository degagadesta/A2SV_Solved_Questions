class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == [2,1]:
            return 1
        mn = nums[0]
        left = -1
        n = len(nums)
        right = n

        while left + 1 < right:
            mid = (right + left) // 2
            if nums[mid] <= mn :
                right = mid
                mn = nums[mid]
            else:
                left = mid
        return mn            

        