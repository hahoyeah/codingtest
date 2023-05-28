def solution(array, commands):
    answer = []
    for v in range(len(commands)):
        i,j,k = commands[v]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
        