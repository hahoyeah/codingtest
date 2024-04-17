import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
d = list(map(int, input().split()))

# 0:+, 1:-, 2:*, 3://
ma = -1e10
mi = 1e10

def dfs(depth,total,plus,minus,multi,div):
    global ma,mi

    if depth == n:
        ma = max(ma,total)
        mi = min(mi,total)

    if plus:
        dfs(depth+1, total+graph[depth], plus-1, minus,multi,div)
    if minus:
        dfs(depth+1, total-graph[depth], plus, minus-1,multi,div)
    if multi:
        dfs(depth+1, total*graph[depth], plus, minus,multi-1,div)
    if div:
        if total<0 and graph[depth]>0:
            dfs(depth+1, -((-total)//graph[depth]), plus, minus,multi,div-1)
        else:
            dfs(depth+1, total//graph[depth], plus, minus,multi,div-1)



dfs(1,graph[0],d[0],d[1],d[2],d[3])
print(ma)
print(mi)