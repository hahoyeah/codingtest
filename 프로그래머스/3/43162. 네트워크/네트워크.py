def solution(n, computers):
    visit = [0]*n
    count = 0
    d = [[] for _ in range(n)]
    
    for i in range(n-1):
        for j in range(i+1,n):
            if computers[i][j]==1:
                d[i].append(j)
                d[j].append(i)
    
    def dfs(graph):
        for k in graph:
            if visit[k]==0:
                visit[k]=1
                dfs(d[k])
    
    for t in range(n):
        if visit[t]==0:
            count += 1
            visit[t]=1
            dfs(d[t])
                
    return count
        