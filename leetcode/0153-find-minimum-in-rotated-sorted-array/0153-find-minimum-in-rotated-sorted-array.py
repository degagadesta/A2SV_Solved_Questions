class Solution:
    def findMin(self, nums: List[int]) -> int:
        mn = nums[0]
        left = -1
        n = len(nums)
        right = n

        while left + 1 < right:
            mid = math.ceil((right + left) / 2)
            if nums[mid] <= mn :
                right = mid
                mn = nums[mid]
            else:
                left = mid
        return mn            

        