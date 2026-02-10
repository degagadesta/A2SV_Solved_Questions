class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums:
                add = 1
                while num + add in nums:
                    add += 1
                ans = max(ans, add)
        return ans
