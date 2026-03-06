class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        summ = 0 
        ans = []

        for i in word :
            summ = summ * 10 + int(i)
            if summ % m == 0 :
                ans.append(1)
            else:
                ans.append(0) 
            summ = summ % m     
        return ans                  
            
        