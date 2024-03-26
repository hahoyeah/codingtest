import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().strip())) for _ in range(n)]

visit = [[0]*n for _ in range(n)]
result=[]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(r,c):
    visit[r][c]=1
    count = 1
    for k in range(4):
        kr = r+dr[k]
        kc = c+dc[k]
        if 0<=kr<n and 0<=kc<n and graph[kr][kc]==1 and visit[kr][kc]==0:
            count += dfs(kr,kc)
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visit[i][j]==0:
            result.append(dfs(i,j))

result.sort()
print(len(result))
for i in result:
    print(i)