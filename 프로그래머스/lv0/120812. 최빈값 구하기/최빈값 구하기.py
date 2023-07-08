def solution(array):
    from collections import Counter, defaultdict
    s = Counter(array)
    ma = 0
    result = 0
    for key in s:
        if s[key]>ma:
            ma=s[key]
            result = key
    c=0
    for key in s:
        if ma==s[key]:
            c+=1
    
    if c>1:
        return -1
    
    return result