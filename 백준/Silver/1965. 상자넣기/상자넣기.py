import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = list(map(int,input().split()))

d = [1] * (n)

for i in range(1,n):
    for k in range(i):
        if graph[k]<graph[i]:
            d[i] = max(d[k]+1, d[i])

print(max(d))