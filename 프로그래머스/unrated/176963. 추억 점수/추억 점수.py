def solution(name, yearning, photo):
    answer = [0] * len(photo)
    dic = dict()
    for i,j in zip(name, yearning):
        dic[i]=j
    for k in range(len(photo)):
        for v in photo[k]:
            if v in dic:
                answer[k] += dic[v]
    return answer