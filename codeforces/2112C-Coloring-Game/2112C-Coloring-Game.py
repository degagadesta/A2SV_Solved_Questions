t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for k in range(2,n):
        temp = max(a[k], a[-1] - a[k])
        l , r = 0 , k -1
        while l < r :
            if a[l] + a[r] > temp :
                cnt += (r - l)
                r -= 1
            else:
                l += 1
    print(cnt)