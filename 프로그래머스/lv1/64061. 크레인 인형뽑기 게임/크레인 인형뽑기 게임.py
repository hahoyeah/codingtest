def solution(board, moves):
    #스택
    #같은거 두개모이면 두개 사라진다
    #moves는 board[0][i]의 인덱스
    stack = []
    answer = 0
    for i in moves:
        i = i-1
        for b in board:
            if b[i] != 0:
                if stack and stack[-1] == b[i]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(b[i])
                b[i] = 0
                break
    return answer
        
