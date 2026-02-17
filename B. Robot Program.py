t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    pr = [0] * n
    for i in range(n):
        move = -1 if s[i] == 'L' else 1
        if i == 0:
            pr[i] = move
        else:
            pr[i] = pr[i-1] + move

    fir = -1
    for i in range(n):
        if x + pr[i] == 0:
            fir = i + 1
            break

    if fir == -1 or fir > k:
        print(0)
        continue

    answer = 1
    r= k - fir

    cyc = -1
    for i in range(n):
        if pr[i] == 0:
            cyc = i + 1
            break

    if cyc == -1:
        print(answer)
    else:
        answer += r// cyc
        print(answer)
