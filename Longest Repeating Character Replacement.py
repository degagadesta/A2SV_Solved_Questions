class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        cnt = defaultdict(int)
        max_cnt = 0
        res = 0
        for right in range(len(s)) :
            cnt[s[right]] += 1
            max_cnt = max(max_cnt , cnt[s[right]])

            while (right - left + 1 - max_cnt) > k :
                cnt[s[left]] -= 1
                left += 1

            res = max(res , right - left + 1)
        return res        
        
