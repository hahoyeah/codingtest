import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

shark = []
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            shark.append((i,j))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count = 100
            for a,b in shark:
                r=abs(i-a)
                c=abs(j-b)
                count = min(max(r,c),count)
            result = max(count,result)

print(result)