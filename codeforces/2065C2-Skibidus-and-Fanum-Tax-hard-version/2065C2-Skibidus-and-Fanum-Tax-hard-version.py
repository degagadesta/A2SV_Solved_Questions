def findB(curr ,mx , b):
        l , r = 0 , len(b)-1
        temp = float("-inf")
        
        while l  <= r :
            mid = (l + r) // 2
            if b[mid] - curr <= mx:
                l = mid + 1
                temp =  b[mid] - curr
            else:
                r = mid -1 
        return temp 
for _ in range(t):
    n , m= map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))                    
    b.sort()
    
    a[-1] = max(a[-1], b[-1] - a[-1])
    fl = 1
    for i in range(n-2, -1, -1):
        t = a[i] if a[i] <= a[i+1] else float("-inf")
        temp = findB(a[i] , a[i+1] , b)
        
        ans = max(t , temp)
        if ans == float("-inf"):
            fl = 0
            break
        a[i] = ans
        
    if fl:
        print("YES")
    else:
        print("NO")