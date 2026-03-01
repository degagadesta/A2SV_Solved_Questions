from collections import defaultdict
n , k = map(int, input().split())
a = list(map(int, input().split()))

temp = set()
cnt = defaultdict(int)
left = 0
ans = 0
for right in range(n) :
    cnt[a[right]] += 1
    temp.add(a[right]) 
    while len(temp) > k :
            cnt[a[left]] -= 1
            if cnt[a[left]] == 0 :
                temp.remove(a[left])
            left += 1    
    ans += right - left + 1
print(ans)            
