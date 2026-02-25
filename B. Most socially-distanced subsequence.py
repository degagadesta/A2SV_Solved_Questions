t = int(input())

for _ in range(t) :
    n = int(input())
    s = list(map(int, input().split()))
    ans = []
    if len(s) > 2:
        ans.append(s[0])
        left = 0
        right = 1
        if s[left] < s[right] :
            inc = 1
        else:
            inc = 0 
        right += 1       
        while right < n:
            if inc :
                if s[right] > s[right-1] :
                    if right == n-1 :
                        ans.append(s[right])
                    right += 1
                    continue
                else :
                    ans.append(s[right-1])
                    if right == n-1 :
                        ans.append(s[right])
                    inc = 0
            else:
                if s[right] < s[right-1] :
                    if right == n-1 :
                        ans.append(s[right])
                    right += 1
                    continue
                else :
                    ans.append(s[right-1])
                    if right == n-1 :
                        ans.append(s[right])
                    inc = 1
            right += 1
    else :
        ans.extend([s[0], s[1]])        
    print(len(ans))  
    print(*ans)          
                       
            
    
            
             
        
            
            
                 
