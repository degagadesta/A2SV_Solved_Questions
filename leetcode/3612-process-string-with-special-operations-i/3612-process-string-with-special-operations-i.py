class Solution:
    def processStr(self, s: str) -> str:
        st = []
        for ch in s:
            if ch == "*":
                if st:
                    st.pop()
            elif ch == "#":
                if st:
                    st.extend(st[:])   
            elif ch == "%":
                st.reverse()
            else:
                st.append(ch)
        ans = "".join(st)
        return ans                          
        