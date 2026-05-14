class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        n = len(nums) - 1
        cnt = [1] * n
        cnt[-1] += 1
        for i in nums:
            if i > n :
                return False
            cnt[i-1] -= 1
        for i in cnt:
            if i != 0:
                return False    
        return True
