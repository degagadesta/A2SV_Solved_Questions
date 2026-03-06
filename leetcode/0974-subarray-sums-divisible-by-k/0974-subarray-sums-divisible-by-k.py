class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)) :
            nums[i] += nums[i-1]
        
        for i in range(len(nums)) :
            nums[i] = nums[i] % k

        cnt = defaultdict(int)
        ans = 0
        cnt[0] += 1
        for i in nums :
            if i in cnt :
                ans += cnt[i]
            cnt[i] += 1

        return ans        
                
        