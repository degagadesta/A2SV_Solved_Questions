from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools
input = sys.stdin.readline


def ii():
    return int(input())

def mm():
    return map(int, input().split())

def ll():
    return list(map(int, input().split()))

def ss():
    return input().strip()
n,k = mm()
a = ll()
b = ll()
temp = defaultdict(list)
for i in range(n):
    temp[a[i]].append(b[i])
idl = []   
done = [] 
for i in temp:
    cost = temp[i]
    cost.sort()
    done.append(i)
    idl.extend(cost[:-1])
idl.sort()
ans = sum(idl[:k-len(done)])
print(ans)