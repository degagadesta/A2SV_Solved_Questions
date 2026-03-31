class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        
        res = []
        low, high = 0, len(nums) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid
        
        if nums[low] == target:
            res.append(low)
        elif nums[high] == target:
            res.append(high)
        else:
            return [-1, -1]  
            
        low, high = 0, len(nums) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid
        
        if nums[high] == target:
            res.append(high)
        elif nums[low] == target:
            res.append(low)
        else:
            res.append(-1)
            
        return res
