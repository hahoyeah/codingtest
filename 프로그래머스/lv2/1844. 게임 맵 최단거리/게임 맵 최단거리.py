def solution(maps):
    from collections import deque
    q = deque()
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    n = len(maps)
    m = len(maps[0])
    visit = [[0]*m for _ in range(n)]
    x,y = 0,0
    visit[x][y]=1
    #L=0
    q.append((x,y))
    
    # while q:
    #     L+=1
    #     for _ in range(len(q)):
    #         x,y = q.popleft()
    #         for i in range(4):
    #             nx = x+dx[i]
    #             ny = y+dy[i]
    #             if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0 and maps[nx][ny]==1:
    #                 x, y = nx, ny
    #                 visit[nx][ny] = L+1    
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0 and maps[nx][ny]==1:
                visit[nx][ny] = visit[x][y]+1
                q.append((nx,ny))

    return visit[n-1][m-1] if visit[n-1][m-1]!=0 else -1
    