n, s = map(int, input().split())
arr = list(map(int, input().split()))
temp = 0
ans = 0
left = 0

for right in range(n):
    temp += arr[right]
    while temp >= s :
        temp -= arr[left]
        ans += n - right 
        left += 1
print(ans)        
        
