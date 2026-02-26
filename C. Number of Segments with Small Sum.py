n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
temp = 0

left = 0 
for right in range(n) :
   if arr[right] <= s :
       ans += 1
   temp += arr[right]
   while temp > s :
       temp -= arr[left]
       left += 1
   if temp != arr[right]  and left <= right:
       ans += right - left 
                      
print(ans)        
