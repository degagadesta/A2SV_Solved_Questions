class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt=Counter(s)
        t_cnt=Counter(t)

        if s_cnt==t_cnt :
            return 0

        cnt=0
        for ch in s_cnt :
            if s_cnt [ch] != t_cnt[ch]:
                cnt += max(0, s_cnt[ch] - t_cnt[ch])
                 
        return cnt           
        
