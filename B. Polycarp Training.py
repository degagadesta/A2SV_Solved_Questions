n = int(input())
a = list(map(int, input().split()))

a.sort()
day = 0
k =1
i = 0
while(i < n):
    while(a[i] < k):
        i += 1
        if i == n :
            break
    if i < n:
        day += 1
        k += 1
    i += 1 
print(day)           
