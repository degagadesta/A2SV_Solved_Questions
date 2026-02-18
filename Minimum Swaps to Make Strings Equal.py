class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
            
        xy = 0
        yx = 0

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x'  :
                xy += 1
            else:
                yx += 1

        if (yx + xy) % 2 != 0 :
            return -1  
        total = (xy//2) + (yx//2) + (2 if yx %2 != 0 else 0 )      
        return total            
