def solution(n):
    #달팽이구조
    r,c = 0,0
    d = 1
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    end = n*n
    cnt=1
    graph = [[0] * n for _ in range(n)]
    graph[0][0]=1
    while cnt < end:
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<n and 0<=nc<n and graph[nr][nc] == 0:
            #graph[nr][nc] == 0이게 뒤에 가야한다.
            cnt += 1
            r = nr
            c = nc
            graph[r][c] = cnt
        else:
            d = (d+1)%4
    return graph

#def solution(n):
#    #달팽이구조
#    r,c = 0,0
#    d = 1
#    dr = [-1,0,1,0]
#    dc = [0,1,0,-1]
#    end = n*n
#    cnt=1
#    graph = [[0] * n for _ in range(n)]
#
#    while cnt < end:
#        nr = r + dr[d]
#        nc = c + dc[d]
#        if nr<0 or nr>=n or 0>nc or nc>=n or graph[nr][nc] != 0:
#            d = (d+1)%4
#            continue
#        graph[r][c] = cnt
#        cnt += 1
#        r = nr
#        c= nc
#    graph[r][c] = cnt    
#        
#    return graph

#print(solution(4))