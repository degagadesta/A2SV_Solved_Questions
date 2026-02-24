from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    t = input()
    
    s_cnt = Counter(s)
    t_cnt = Counter(t)
    temp = []
    fl = 0
    #print(s[2])
    for i in s_cnt :
        if i not in t_cnt :
            fl = -1
            break
    for i in t_cnt :
        if t_cnt[i] < s_cnt[i] :
            fl = -1
            break
        else:
            t_cnt[i] -= s_cnt[i]
            while t_cnt[i] > 0 :
                temp.append(i)
                t_cnt[i] -= 1
    if fl != -1 :
        ans = []
        l = 0
        r = 0
        temp.sort()
        #print(temp)
        while l < len(temp) and r < len(s) :
            if temp[l] < s[r] :
                ans.append(temp[l])
                l += 1
            else:
                ans.append(s[r])
                r += 1
        #print(ans)        
        ans.extend(temp[l:])
        while r < len(s):
            ans.append(s[r])
            r += 1
    print("".join(ans) if fl != -1 else "Impossible")                                 
            
                
    
