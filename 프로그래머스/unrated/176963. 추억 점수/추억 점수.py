def solution(name, yearning, photo):
    from collections import defaultdict
    dic = defaultdict(int)
    result = [0]*len(photo)
    for i,j in zip(name,yearning):
        dic[i] = j
    for k in range(len(photo)):
        for v in photo[k]:
            result[k] += dic[v]
    return result