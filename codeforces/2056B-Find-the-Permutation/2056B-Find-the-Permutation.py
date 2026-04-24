from collections import defaultdict, deque, Counter
import math, sys, bisect, itertools
input = sys.stdin.readline


def it():
    return int(input())

def ma():
    return map(int, input().split())

def li():
    return list(map(int, input().split()))

def st():
    return input().strip()
t = it()
for _ in range(t):
    n = it()
    ans = [0] * n
    for i in range(n):
        
        left = 0
        stt = st()
        
        for j in range(len(stt)):
            if (stt[j] == "1" and j < i) or (stt[j] == "0" and j >  i):
                left += 1
        ans[left] = i + 1 
        
    print(*ans)