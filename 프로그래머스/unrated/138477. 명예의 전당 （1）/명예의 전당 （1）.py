def solution(k, score):
    ks = []
    answer = []
    for i in score:
        if len(ks) < k:
            ks.append(i)
        elif min(ks) < i:
            ks.sort()
            ks[0] = i
        answer.append(min(ks))
    return answer