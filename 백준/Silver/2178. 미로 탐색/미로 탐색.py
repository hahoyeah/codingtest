import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

start = (0,0)

dr = [0,1,0,-1]
dc = [1,0,-1,0]
visit = [[0]*m for _ in range(n)]
visit[0][0]=1

q = deque()
q.append(start)

while q:
    r,c = q.popleft()

    if r==n-1 and c==m-1:
        break  

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<n and 0<=nc<m and graph[nr][nc]==1 and visit[nr][nc]==0:
            visit[nr][nc] = visit[r][c] + 1
            q.append((nr,nc))

print(visit[n-1][m-1]) 