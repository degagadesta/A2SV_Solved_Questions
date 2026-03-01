t = int(input())
for _ in range(t) :
    n , k = map(int, input().split())
    a = input()
    left = 0
    ans = 0
    cnt = 0
    for right in range(n) :
        if a[right ] == "B" :
            cnt += 1
        ans = max(ans , cnt)
        if right >= k - 1 :
            if a[left] == "B" :
                cnt -= 1
            left += 1
    print(k - ans)                
