def solution(n, m, section):
    result = 1
    t = section[0]
    for i in range(1,len(section)):
        s = section[i] - t
        if s >= m:
            result += 1
            t = section[i]
    return result