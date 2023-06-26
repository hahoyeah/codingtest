def solution(park, routes):
    #split() 이용
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    d = {'N':0, 'S':2, 'W':3, 'E':1}
    n = len(park)
    m = len(park[0])
    r,c = 0,0
        
    for i in range(n): # 행
        for j in range(m): # 열
            if park[i][j] == "S":
                r,c = i,j
               
    for k in routes:
        a,b = k.split()
        b = int(b)
        lr,lc = r,c 
        for _ in range(b):
            nr = r + dr[d[a]]
            nc = c + dc[d[a]]
            if nr<0 or nr>=n or nc<0 or nc>=m or park[nr][nc]=="X":
                r,c = lr,lc
                break
            r = nr
            c = nc
    
    return [r,c]