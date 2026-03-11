bra = input()
st = [-1] 
ans = 0
cnt = 1

for i, char in enumerate(bra):
    if char == "(":
        st.append(i)
    else:
        st.pop()
        if not st:
            st.append(i)  
        else:
            length = i - st[-1]
            if length > ans:
                ans = length
                cnt = 1
            elif length == ans and length > 0:
                cnt += 1

if ans == 0:
    print(0, 1)
else:
    print(ans, cnt)