import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m,n,k = map(int,input().split())
d = [[0]*(n+1) for _ in range(m+1)]
result = []

for _ in range(k):
    c1,r1,c2,r2 = map(int,input().split())
    r1 = m-r1
    r2 = m-r2
    for i in range(r2,r1):
        for j in range(c1,c2):
            d[i][j]=1

def dfs(r,c):
    if 0<=r<m and 0<=c<n and d[r][c]==0:
        d[r][c]=1
        a = dfs(r+1,c)
        b = dfs(r-1,c)
        e = dfs(r,c+1)
        f = dfs(r,c-1)
        return a+b+e+f+1
    else:
        return 0

for i in range(m):
    for j in range(n):
        if d[i][j]==0:
            result.append(dfs(i,j))

result.sort()
print(len(result))
print(' '.join(map(str,result)))