def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    if len(score) < m:
        return answer
    for i in range(1,len(score)//m+1):
        answer += min(score[m*(i-1):m*i]) * m
    return answer