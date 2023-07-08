def solution(n):
    d = [[0]*n for _ in range(n)]
    d[0][0]=1
    L=1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    r,c = 0,0
    i = 1
    
    while L<n*n:
        nr = r+dx[i]
        nc = c+dy[i]
        if 0<=nr<n and 0<=nc<n and d[nr][nc]==0:
            L+=1
            d[nr][nc] = L
            r,c = nr,nc
        else:
            i = (i+1)%4
    return d
            