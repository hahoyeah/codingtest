def solution(maps):
    from collections import deque
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    q = deque()
    n = len(maps)
    m = len(maps[0])
    dist = [[0]*m for _ in range(n)]
    L = 1
    q.append([0,0])
    maps[0][0] = 0
    # 도착지점 n-1, m-1
    while q:
        l = len(q)
        for _ in range(l):
            r,c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<n and 0<=nc<m and maps[nr][nc] == 1:
                    maps[nr][nc] = 0
                    q.append([nr,nc])
                    dist[nr][nc] = L+1
        L+=1
    return dist[n-1][m-1] if dist[n-1][m-1]!=0 else -1
                    
                    
            