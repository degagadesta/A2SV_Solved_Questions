class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = []
        ans = 0
        for i in s :
            if i == "(" :
                score.append(0)
            else :
                val = score.pop()
                if val == 0:
                    temp = 1
                else:
                    temp = val * 2
                if score:
                    score[-1] += temp
                else:
                    score.append(temp)
                  
        return score[0]                    
        