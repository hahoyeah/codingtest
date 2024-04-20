import sys
input = sys.stdin.readline

N,L = map(int,input().split())
graph = list(map(int,input().split()))
graph.sort()

count = 1
s = graph[0]

for i in range(1,N):
    if graph[i]-s >= L:
        count += 1
        s = graph[i]

print(count)