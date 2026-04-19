class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            t = abs(nums[i])
            if nums[t-1] < 0:
                ans.append(t)
            else:
                nums[t-1] *= -1
        return ans                    