class Solution:
    def splitString(self, s: str) -> bool:
        temp = []
        def backtrack(ind):
            if ind >= len(s):
                for i in range(1, len(temp)):
                    if temp[i-1] - temp[i] != 1:
                        return False
                return len(temp) >= 2        
            for i in range(ind, len(s)):
                val = int(s[ind:i+1])
                temp.append(val)
                if backtrack(i+1):
                    return True
                temp.pop()        
            return False
        return backtrack(0)            
        