n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

right = 0
ans = 0
cnt = 0
for i in range(n):
    if i != 0  and a[i] == a[i-1] :
        ans += cnt
        
    else  :
        cnt = 0
        while  right < m  and a[i] > b[right] :
            right += 1
    
        while right < m and  a[i] == b[right] :
            cnt += 1 
            ans += 1
            right += 1
                        
print(ans )                
