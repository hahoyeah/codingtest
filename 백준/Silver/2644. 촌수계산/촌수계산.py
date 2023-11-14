import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a,b = map(int, input().split())
m = int(input())
graph = {i:[] for i in range(n+1)}

for _ in range(m):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def bfs(a,b,graph):
    v = [0]*(n+1)
    q = deque()
    q.append((a,0))
    
    while q:
        current, count = q.popleft()
        v[current]=1
        if b ==current:
            return count
        for i in graph[current]:
            if v[i]==0:
                q.append((i,count+1))
    return -1
        
print(bfs(a,b,graph)) 