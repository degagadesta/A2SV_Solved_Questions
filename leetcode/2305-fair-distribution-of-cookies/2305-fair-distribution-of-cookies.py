class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mn = float("inf")
        summ = [0] * k

        def helper(idx):
            nonlocal mn
            if idx >= len(cookies):
                mn = min(mn ,max(summ))
                return 
            if mn <= max(summ):
                return    
            for i in range(k):
                summ[i] += cookies[idx]
                helper(idx+1)
                summ[i] -= cookies[idx]

        helper(0)
        return mn        
        