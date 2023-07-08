def solution(survey, choices):
    from collections import defaultdict
    dic = defaultdict(int)
    left = ['R','C','J','A']
    right = ['T','F','M','N']
    result = ''

    for i,j in zip(left,right):
        dic[i]
        dic[j]
        
    num = [3,2,1,0,1,2,3]
    
    for s,ch in zip(survey,choices):
        if ch>3:
            dic[s[1]] += num[ch-1]
        else:
            dic[s[0]] += num[ch-1]
    
    for i,j in zip(left,right):
        if dic[i]>=dic[j]:
            result += i
        else:
            result += j
            
    return result