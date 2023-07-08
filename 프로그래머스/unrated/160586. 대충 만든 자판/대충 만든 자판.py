def solution(keymap, targets):
    from collections import defaultdict
    dic = defaultdict(int)
    result = [0]*len(targets)
    
    for i in keymap:
        for ind, key in enumerate(i):
            ind = ind+1
            if key in dic and dic[key]>ind:
                dic[key] = ind
            if key not in dic:
                dic[key] = ind
    
    for k in range(len(targets)):
        for key in targets[k]:
            result[k] += dic[key]
            if dic[key] == 0:
                result[k] = -1
                break
    return result