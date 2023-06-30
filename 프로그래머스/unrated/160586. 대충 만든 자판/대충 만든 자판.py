def solution(keymap, targets):
    from collections import defaultdict
    dic = defaultdict(int)
    result = [0]*len(targets)
    
    for key in keymap:
        for i in range(len(key)):
            if dic[key[i]] > i+1 or dic[key[i]]==0:
                dic[key[i]] = i+1
    for t in range(len(targets)):
        for k in targets[t]:
            if dic[k] == 0:
                result[t] = -1
                break
            else:
                result[t] += dic[k]
    return result