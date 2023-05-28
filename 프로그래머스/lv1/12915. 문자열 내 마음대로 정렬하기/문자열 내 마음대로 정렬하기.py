def solution(strings, n):
    sn = []
    for i,v in enumerate(strings):
        sn.append(v[n] + v)
    sn.sort()
    for i in range(len(sn)):
        sn[i] = sn[i][1:]
    return sn