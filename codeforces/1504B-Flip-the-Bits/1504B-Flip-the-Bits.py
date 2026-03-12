t = int(input())
for _ in range(t) :
    n = int(input())
    a = list(map(int, input().strip()))
    b = list(map(int,input().strip()))
    prefix=[int(a[0])]
    for i in range(1, n):
        prefix.append(prefix[i-1]+int(a[i]))

    flip=0
    flag=1

    for i in range(n-1, -1, -1):
        if (not flip and a[i]==b[i]) or (flip and a[i]!=b[i]):
            continue
        
        if not flip and a[i]!=b[i] and prefix[i]==i+1-prefix[i]:
            flip= (flip + 1) % 2
        elif flip and a[i]==b[i] and prefix[i]==i+1-prefix[i]:
            flip= (flip + 1 ) % 2
        else:
            flag=0
            break

    if flag:
        print("YES")
    else:
        print('NO')