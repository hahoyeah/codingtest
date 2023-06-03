def solution(answers):
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    sum_abc = [0,0,0]
    result = []
    for i,j,k,v in zip(a,b,c,answers):
        if i == v:
            sum_abc[0] += 1
        if j == v:
            sum_abc[1] += 1
        if k == v:
            sum_abc[2] += 1
    for i in range(len(sum_abc)): #.index(i)
        if sum_abc[i] == max(sum_abc):
            result.append(i + 1)
    return sorted(result)
        