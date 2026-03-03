from collections import defaultdict

n, k, q = map(int, input().split())

cnt = defaultdict(int)
min_l = float("inf")
max_r = 0

for _ in range(n):
    l, r = map(int, input().split())
    cnt[l] += 1
    cnt[r + 1] -= 1
    if l < min_l: min_l = l
    if r > max_r: max_r = r

temp = [0 for i in range(min_l, max_r + 2)]
for i in cnt:
    if min_l <= i <= max_r + 1:
        temp[i - min_l] += cnt[i]

for i in range(1, len(temp)):
    temp[i] += temp[i-1]

fin = []
for i in temp:
    if i >= k:
        fin.append(1)
    else:
        fin.append(0)

for i in range(1, len(fin)):
    fin[i] += fin[i-1]

for _ in range(q):
    a, b = map(int , input().split())
    
    actual_a = max(a, min_l)
    actual_b = min(b, max_r)
    
    if actual_a > actual_b:
        print(0)
    else:
        idx_b = actual_b - min_l
        idx_a_minus_1 = actual_a - min_l - 1
        
        val_b = fin[idx_b]    
        val_a = fin[idx_a_minus_1] if idx_a_minus_1 >= 0 else 0
        
        print(val_b - val_a)