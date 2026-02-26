from collections import Counter
t = int(input())
for _ in range(t) :
    n , l , r = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left = arr[:l]
    right = arr[l:]
    cnt1 = Counter((left))
   
    cnt2 = Counter(right)
    ans = n//2 - min(l, r)
    
    if l > r :
        dif = ans
        for i in cnt1 :
            if cnt1[i] > cnt2[i] + 1:
                t = (cnt1[i] - cnt2[i] ) // 2
                t = min(t, dif)
                cnt1[i] -= t
                cnt2[i] += t
                dif = dif - t
        temp = dif
        
        
        for i in cnt1 :
            if cnt1[i] > cnt2[i] and temp :
                cnt1[i] -= 1
                cnt2[i] += 1
                temp -= 1
                        
    elif r > l:
        dif = ans
        for i in cnt2 :
            if cnt2[i] > cnt1[i] + 1:
                t = (cnt2[i] - cnt1[i] )//2
                
                t = min(dif, t)
                cnt2[i] -= t
                cnt1[i] += t   
                dif = dif - t     
        temp = dif 
        for i in cnt2 :
            if cnt2[i] > cnt1[i] and temp:
                temp -= 1
                cnt1[i] += 1
                cnt2[i] -= 1
                
    for l in cnt1 :
        if cnt1[l] > cnt2[l] :
            ans += cnt1[l] - cnt2[l]
    
    print(ans)            
            
            
            
              
        
