from collections import Counter
def solution(array):
    cnt = Counter(array)
    max_cnt = max(cnt.values())
    
    len_max = [[i,v] for i,v in cnt.items() if max_cnt==v]
    if len(len_max) > 1:
        return -1

    return len_max[0][0]