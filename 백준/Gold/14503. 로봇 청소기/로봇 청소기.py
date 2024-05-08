import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

# 처음 좌표와 바라보는 방향
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 1은 벽, 0은 청소 안한 칸
dr = [-1,0,1,0] # 북,동,남,서
dc = [0,1,0,-1]

def dfs(r,c,d):
    if graph[r][c]==0:
        graph[r][c]=2
    for i in range(4):
        k = (d+3-i)%4
        a = r+dr[k]
        b = c+dc[k]       
        if 0<=a<n and 0<=b<m and graph[a][b]==0:
            count = dfs(a,b,k)
            return count + 1
    e = (d+2)%4
    f = r+dr[e]
    g = c+dc[e]
    if 0<=f<n and 0<=g<m and graph[f][g]==2:
        s = dfs(f,g,d)
        return s
    else:
        return 0

print(dfs(r,c,d)+1)