n , k = map(int, input().split())
arr = list(map(int, input().split()))

temp = [arr[i] - arr[i-1] for i in range(1, len(arr))]
temp.sort()

ans = 0
for i in range(len(temp)-k+1) :
    ans += temp[i]
print(ans)    
