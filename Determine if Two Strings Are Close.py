class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) :
            return False
        temp1=Counter(word1)
        temp2=Counter(word2) 

        for i in temp1:
            if i not in temp2:
                return False      

        for i in temp2:
            if i not in temp1:
                return False
           
        cnt1 = sorted(temp1.values())
        cnt2 = sorted(temp2.values())
        return cnt1 == cnt2   

        
