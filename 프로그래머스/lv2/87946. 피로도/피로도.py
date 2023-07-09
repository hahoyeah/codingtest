def solution(k, dungeons):
    import sys
    sys.setrecursionlimit(int(1e6))
    
    d = [0]*len(dungeons)
    result = 0
    
    def DFS(k, cnt):
        nonlocal result
        result = max(cnt,result)
        for i in range(len(d)):
            if k>=dungeons[i][0] and d[i]==0:
                d[i]=1
                DFS(k-dungeons[i][1],cnt+1)
                d[i] = 0
        
    DFS(k,0)
    
    return result