import sys
# 이거 안쓰면 최대 재귀 깊이보다 더 깊어져서 오류난다
sys.setrecursionlimit(10000) # 재귀의 깊이를 설정(기본1000)
input = sys.stdin.readline

t = int(input())
result = [0]*t

for c in range(t):
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    xy=[]
    for _ in range(k):
        a,b = map(int, input().split())
        graph[b][a]=1 # b가 세로길이(n), a가 가로길이(m)
        xy.append((b,a))

    visit = [[0]*m for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    def dfs(x,y): # x<n, y<m
        s=0
        if 0<=x<n and 0<=y<m and visit[x][y]==0 and graph[x][y]==1:
            visit[x][y]=1
            for v in range(4):
                s += dfs(x+dx[v],y+dy[v])
            return 1+s
        else:
            return 0


    for i,j in xy:
        size = dfs(i,j)
        if size>0:
            result[c] += 1
for count in result:
    print(count)