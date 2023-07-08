def solution(park, routes):
    n = len(park)
    m = len(park[0])
    dic = {
        'N':(-1,0),
        'S':(1,0),
        'W':(0,-1),
        'E':(0,1)
    }
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                r,c = i,j
    kr,kc = r,c            
    for k in routes:
        op, count = k.split()
        for _ in range(int(count)):
            nr = kr + dic[op][0]
            nc = kc + dic[op][1]
            if 0<=nr<n and 0<=nc<m and park[nr][nc]!='X':
                kr,kc = nr,nc
            else:
                kr,kc = r,c
                break
        r,c = kr,kc
    
    return r,c

        
        
    
    