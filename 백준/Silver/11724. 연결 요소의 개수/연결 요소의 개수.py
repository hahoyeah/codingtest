import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
d = [[] for _ in range(n)]

def dfs(k):
    visit[k]=1
    for s in d[k]:
        if visit[s]==0:
            dfs(s)


for i,j in graph:
    d[i-1].append(j-1)
    d[j-1].append(i-1)

visit = [0]*n
count = 0

for k in range(n):
    if visit[k]==0:
        count+=1
        dfs(k)

print(count)