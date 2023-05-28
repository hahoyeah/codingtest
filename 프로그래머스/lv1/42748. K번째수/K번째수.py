def solution(array, commands):
    answer = []
    for v in range(len(commands)):
        i,j,k = commands[v][0], commands[v][1], commands[v][2]
        a = array[i-1:j]
        a.sort()
        answer.append(a[k-1])
    return answer
        