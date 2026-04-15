class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        mx = 0
        ans = []
        def is_valid(s):
            temp = []
            for i in s:
                if i =="(":
                    temp.append(i)
                elif i == ")":
                    if not temp:
                        return False
                    temp.pop()
            return not temp 
        def backtrack(idx, temp):
            nonlocal mx, ans
            if idx == len(s):

                if len(temp) >= mx and is_valid(temp):
                    if len(temp) > mx:
                        mx = len(temp)
                        ans =["".join(temp.copy())] 
                    if len(temp) == mx:
                        ans.append("".join(temp.copy()))
                return  
            if s[idx] != "(" and s[idx] != ")":
                temp.append(s[idx])
                backtrack(idx+1, temp)
                temp.pop()
            else:
                temp.append(s[idx])
                backtrack(idx+1, temp)
                temp.pop()
                backtrack(idx+1, temp)
        backtrack(0, []) 
        ans = set(ans)
        ans = list(ans)       
        return ans                   

