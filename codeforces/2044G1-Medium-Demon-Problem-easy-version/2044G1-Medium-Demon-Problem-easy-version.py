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
t = ii()
for _ in range(t):
    n = ii()
    indegree = [0] * n
    graph = [[] for i in range(n)]
    r = list(mm())
    for i in range(n):
        graph[i].append(r[i] - 1)
        indegree[r[i] - 1] += 1
    
    year = 2
    queue = deque()
    for i in range(n):
        if not indegree[i]:
            queue.append(i)
    while queue:
        length = len(queue)
        for _ in range(length):
            node = queue.popleft()
            for adj in graph[node]:
                indegree[adj] -= 1
                if not indegree[adj]:
                    queue.append(adj)
        year += 1  
    print(year)