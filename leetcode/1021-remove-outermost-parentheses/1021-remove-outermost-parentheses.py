class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        st =[]
        for par in s:
            if par == "(":
                if st:
                    ans.append(par)
                st.append(par)
            else:
                st.pop()
                if st:
                    ans.append(par)
        res = "".join(ans)
        return res        
                        