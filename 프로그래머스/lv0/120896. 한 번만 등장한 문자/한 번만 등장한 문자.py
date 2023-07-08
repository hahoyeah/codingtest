def solution(s):
    from collections import Counter
    result = []
    count = Counter(s)
    for key in count:
        if count[key] == 1:
            result.append(key)
            
    return "".join(sorted(result))        
