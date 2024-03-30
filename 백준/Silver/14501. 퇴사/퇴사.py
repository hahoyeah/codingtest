import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

d = [0] * 1001

a,b = graph[0]
for i in range(a):
    if i < n:
        d[i] = graph[i][1]

for k in range(n):
    t,p = graph[k]
    if k+t > n:
        d[k]=0
        continue
    else:
        for i in range(k+t,n):
            d[i] = max(d[i],d[k]+graph[i][1])

print(max(d))