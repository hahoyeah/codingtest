def solution(board):
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    n = len(board)
    answer = n*n
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                count += 1
                for k in range(8):
                    nr = dr[k] + i
                    nc = dc[k] + j
                    if 0<=nr<n and 0<=nc<n and board[nr][nc]==0:
                        count += 1
                        board[nr][nc] = 2 
    return answer - count
            
            