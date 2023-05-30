def solution(s):
    p = [] #처음인것들
    answer = [0]*len(s)
    for i,v in enumerate(s):
        if v not in p:
            p.append(v)
            answer[i] = -1
        for j in range(i+1, len(s)):
            if v == s[j]:
                answer[j] = j-i
    return answer