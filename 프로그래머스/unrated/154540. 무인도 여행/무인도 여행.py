import sys
sys.setrecursionlimit(int(1e6))

def solution(maps):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    n = len(maps)
    m = len(maps[0])
    visit = [[0]*m for _ in range(n)]
    result = []
    
    def DFS(x,y):
        s = 0
        if 0<=x<n and 0<=y<m and maps[x][y]!='X' and visit[x][y]==0:
            visit[x][y]=1
            for i in range(4):
                s += DFS(x+dx[i],y+dy[i])
            return s + int(maps[x][y])
        else:
            return 0
        
    for i in range(n):
        for j in range(m):
            size = DFS(i,j)
            if size>0:
                result.append(size)
    
    return sorted(result) if result else [-1]
                