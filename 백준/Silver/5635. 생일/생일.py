import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().split()) for _ in range(n)]

for i in range(n):
    name, dd, mm, yy = graph[i]
    graph[i][1] = int(dd)
    graph[i][2] = int(mm)
    graph[i][3] = int(yy)

graph.sort(key = lambda v : (v[3],v[2],v[1]))

print(graph[-1][0])
print(graph[0][0])