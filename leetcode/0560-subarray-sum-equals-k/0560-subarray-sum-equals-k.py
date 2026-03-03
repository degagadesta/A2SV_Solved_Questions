class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = 0
        cnt = defaultdict(int)
        ans = 0
        cnt[0] += 1

        for i in range(len(nums)) :
            cur += nums[i] 
            if cur - k in cnt :
                ans += cnt[cur - k]

            cnt[cur] += 1             
        return ans         

        