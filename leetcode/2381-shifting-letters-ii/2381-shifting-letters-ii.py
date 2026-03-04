class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        change = [0] * len(s)
        for i, j ,k in shifts :
            change[i] += 1 if k == 1 else -1
            if j < len(s) - 1:
                change[j +1] -= 1 if k == 1 else -1
        tot = 0        
        for i in range(len(change)) :
            tot += change[i]
            change[i] = tot

        ans =[]
        for i in range(len(s)) :
            ch = chr(97 + (ord(s[i]) - 97 + change[i]) % 26)
            ans.append (ch)  

        return "".join(ans)      

        
        