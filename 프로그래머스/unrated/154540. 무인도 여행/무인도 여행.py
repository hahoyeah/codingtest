#런타임 에러를 안나게 해준다.
# 즉 깊이 파고들 수 있게끔 도와준다
# 런타임 에러를 안나게 해주는 스킬!
import sys
sys.setrecursionlimit(int(1e6)) #1e9

def solution(maps):
    #지도, 집개수 이런건 무조건 dfs
    result = []
    n = len(maps)
    m = len(maps[0])
    v = [[0]*m for _ in range(n)]
    
    def DFS(x,y):
        if 0<=x<n and 0<=y<m and v[x][y]==0 and maps[x][y]!='X':
            v[x][y] = 1
            a = DFS(x+1,y)
            b = DFS(x-1,y)
            c = DFS(x,y+1)
            d = DFS(x,y-1)
            return a+ b+ c+ d+ int(maps[x][y])
        else:
            return 0
        
    for i in range(n):
        for j in range(m):
            size = DFS(i,j)
            if size > 0:
                result.append(size)
    
    return sorted(result) if len(result)>0 else [-1]
