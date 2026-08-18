class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        cnt = Counter(nums)
        if k == 1:
            ans = -1
            for num in nums:
                if cnt[num] == 1 and num > ans:
                    ans = num
            return ans
        ans = - 1
        if cnt[nums[0]] == 1 :
            ans = nums[0]
        if cnt[nums[-1]] == 1 and nums[-1] > ans:
            ans = nums[-1]
        return ans                             