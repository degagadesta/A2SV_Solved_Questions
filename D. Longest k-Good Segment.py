from collections import defaultdict
n , k = map(int , input().split())
a = list(map(int, input().split()))

l , r = 0 , 0
ans = 0
cnt = 0
left = 0
temp = set()
t = defaultdict(int)
for right in range(n) :
    temp.add(a[right])
    t[a[right]] += 1
    while len(temp) > k :
        t[a[left]] -= 1
        if t[a[left]] == 0 :
            temp.remove(a[left])
        left += 1
    
    if right - left + 1 >= ans :
        l = left + 1
        r = right + 1 
        ans = right - left + 1
print(l , r)               
    
