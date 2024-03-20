import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
d = [list(map(int,input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]

for i,j in d:
    graph[i].append(j)
    graph[j].append(i)

answer = 0

def ans(g,k, answer):
    if g:
        for i in g:
            if i not in k:
                k.append(i)
                answer = ans(graph[i],k,answer) + 1

    return answer

print(ans(graph[1],[1],answer))