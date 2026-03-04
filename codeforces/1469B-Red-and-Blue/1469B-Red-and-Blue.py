t = int(input())
for _ in range(t) :
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))
    
    ans = 0
    total = 0
    r , b = 0 , 0
    temp1 = [red[0]]
    total = red[0]
    for i in range(1, n) :
        total += red[i]
        temp1.append(total)
    
    temp2 = [blue[0]]
    total = blue[0]
    for i in range(1, m) :
        total += blue[i]
        temp2.append(total)
    
    res1 = max(0 , max(temp1))
    res2 = max(0, max(temp2)) 
    print(res1 + res2)