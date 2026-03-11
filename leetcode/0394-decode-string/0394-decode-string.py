class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        num = []
        opened = 0
        for i in range(len(s)) :
            if s[i] >= "0" and s[i] <= "9" :
                if i < len(s) - 1 and s[i + 1] != "[" :
                    num.append(s[i])
                else:
                    num.append(s[i])
                    st.append("".join(num)) 
                    num = []
            elif s[i] == "[":
                opened += 1   
            elif s[i] == "]" and opened:
                temp = []
                while st and st[-1][0] >= "a" and st[-1][0] <= "z" :
                    temp.append(st.pop())
                n = int(st.pop())
                temp.reverse()
                temp = (temp) * n
                st.extend(temp)  
                opened -= 1
            else:
                st.append(s[i])
        return "".join(st)              


           
        