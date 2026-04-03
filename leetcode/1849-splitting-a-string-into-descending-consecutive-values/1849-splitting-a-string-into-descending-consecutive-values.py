class Solution:
    def splitString(self, s: str) -> bool:
        def helper(ind , comb):
            if ind >= len(s):
                for i in range(1 , len(comb)):
                    if comb[i - 1]  - comb[i] != 1:
                        return False
                return len(comb) >= 2
            for i in range(ind , len(s)):
                val = int(s[ind : i+1])
                comb.append(val)
                if helper(i + 1, comb):
                    return True
                comb.pop()    
            return False    
        return helper(0 , [])



        