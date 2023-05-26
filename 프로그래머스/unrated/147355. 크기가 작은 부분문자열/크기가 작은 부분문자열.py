def solution(t, p):
    count = 0
    s=''
    for v in range(len(t)):
        if len(p)+v <= len(t):
            for i in range(v,len(p)+v):
                s += t[i]
            if s and int(s)<=int(p):
                count += 1
                s=''
            if s and int(s)>int(p):
                s=''
    return count