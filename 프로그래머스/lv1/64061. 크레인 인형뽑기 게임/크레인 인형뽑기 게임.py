def solution(board, moves):
    stack=[]
    n = len(board)
    result = 0
    
    for j in moves: #열
        j = j-1
        for i in range(n): #행
            if stack and stack[-1]==board[i][j]:
                stack.pop()
                board[i][j]=0
                result += 2
                break
                
            if board[i][j]!=0:
                stack.append(board[i][j])
                board[i][j]=0
                break
                
    return result