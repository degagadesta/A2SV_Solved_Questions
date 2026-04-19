import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        l, r = 0, len(nums) - 1
        
        while l <= r:
            pivot = nums[random.randint(l, r)]
            lt = l      
            i = l       
            gt = r      
            
            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            
            if lt <= target <= gt:
                return nums[target]
            elif target < lt:
                r = lt - 1
            else:
                l = gt + 1
