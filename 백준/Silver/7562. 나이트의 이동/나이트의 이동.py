import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

m = int(input())

r = [-1,-2,-2,-1,1,2,2,1]
c = [2,1,-1,-2,-2,-1,1,2]
result = []

def bfs(graph,n,a,b,x,y):
    queue = deque([(a,b)])

    while queue:
        i,j = queue.popleft()

        if i==x and j==y:
            return graph[x][y]

        for k in range(8):
            dr = i + r[k]
            dc = j + c[k]
            if 0<=dr<n and 0<=dc<n and graph[dr][dc]==0:
                graph[dr][dc] = graph[i][j]+1
                queue.append((dr,dc))


for k in range(m):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    a,b = map(int,input().split())
    x,y = map(int,input().split())
    result.append(bfs(graph,n,a,b,x,y))

for i in result:
    print(i)