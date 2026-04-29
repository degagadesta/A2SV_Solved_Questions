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

n = ii()
word = []
for i in range(n):
    word.append(ss())
graph = [[] for i in range(26)]
impo = False
indegree = [0] * 26
for i in range(n-1):
    j = 0
    while j < len(word[i]) and j < len(word[i+1]) and word[i][j] == word[i+1][j]:
        j += 1
    if j != len(word[i]) and j != len(word[i+1]):
        graph[ord(word[i][j]) - 97].append(word[i+1][j])
        indegree[ord(word[i + 1][j]) - 97] += 1
    elif j != len(word[i]) and j == len(word[i+1]):
        print("Impossible")
        exit()
queue = deque()
for i in range(26):
    if not indegree[i]:
        queue.append(i) 
order = []
while queue:
    node = queue.popleft()
    order.append(chr(node + 97)) 
    for adj in graph[node]:
        indegree[ord(adj) - 97] -= 1
        if not indegree[(ord(adj) - 97)]:
            queue.append(ord(adj) - 97)
print("".join(order) if len(order) == 26 else "Impossible")