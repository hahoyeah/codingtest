import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
max_num = 0
graph = []
for _ in range(n):
    k = list(map(int,input().split()))
    graph.append(k)
    max_num = max(max_num,max(k))

r = [0,1,0,-1]
c = [-1,0,1,0]
d = [0]*(max_num)

def dfs(i,j,k):
    for v in range(4):
        dr = r[v]+i
        dc = c[v]+j
        if 0<=dr<n and 0<=dc<n and visit[dr][dc]==0 and graph[dr][dc]>k:
            visit[dr][dc]=1
            dfs(dr,dc,k)

for k in range(max_num):
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>k and visit[i][j]==0:
                d[k]+=1
                visit[i][j]=1
                dfs(i,j,k)

print(max(d))