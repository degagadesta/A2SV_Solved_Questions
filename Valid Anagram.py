class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp1 = Counter(s)
        temp2 = Counter(t)

        for i in temp1:
            if i not in temp2:
                return False
            else:
                if temp1[i] !=temp2[i]:
                    return False 
                     
        return True    

        
