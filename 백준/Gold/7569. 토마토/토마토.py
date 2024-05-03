import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

visit = [[[0]*m for _ in range(n)] for _ in range(h)]

dm = [0,0,1,0,-1,0] # 가로
dn = [0,0,0,-1,0,1] # 세로
dh = [-1,1,0,0,0,0] # 높이
queue = deque()

def bfs(visit,leng):
    global queue
    while queue:
        for _ in range(len(queue)):
            i,j,k = queue.popleft()
            for v in range(6):
                dc = dm[v]+k
                dr = dn[v]+j
                dl = dh[v]+i
                if 0<=dl<h and 0<=dr<n and 0<=dc<m and graph[dl][dr][dc]==0 and visit[dl][dr][dc]==0:
                    graph[dl][dr][dc]=1
                    visit[dl][dr][dc]=1
                    queue.append([dl,dr,dc])  
        if queue:
              leng += 1

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k]==0:
                    return -1
    return leng

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1 and visit[i][j][k]==0:
                visit[i][j][k]=1
                queue.append([i,j,k])

print(bfs(visit,0))