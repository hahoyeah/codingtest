def solution(board):
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    result = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(len(dx)):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                        board[nx][ny] = 2
    
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                result += 1
    
    return result