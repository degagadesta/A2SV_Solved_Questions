from collections import Counter,defaultdict
n = int(input())
par = []
for i in range(n-1):
    a = int(input())
    par.append(a)
parent = set(par) 
parent.add(1)
temp = defaultdict(list)
v = 2
for i in par:
    if v not in parent:
        temp[i].append(v)
    v += 1
for i in temp:
    if len(temp[i] ) < 3:
        print("No")
        break
else:
    if len(parent) == len(temp):
        print("Yes")   
    else:
        print("No")