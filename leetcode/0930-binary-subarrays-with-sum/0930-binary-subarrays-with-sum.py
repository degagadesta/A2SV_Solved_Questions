class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = defaultdict(int)
        cnt[0] += 1
        tot = 0
        ans = 0
        for num in nums :
            tot += num
            if tot - goal in cnt :
                ans += cnt[tot - goal]

            cnt[tot]  += 1
        return ans     
        