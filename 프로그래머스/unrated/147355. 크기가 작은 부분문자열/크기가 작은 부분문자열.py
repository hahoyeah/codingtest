# def solution(t, p):
#     count = 0
#     for v in range(len(t)-len(p)+1):
#         s = t[v:len(p)+v]
#         if s and int(s)<=int(p):
#             count += 1
#     return count

# def solution(t, p):
#     count = 0
#     for v in range(len(t)):
#         s = t[v:len(p)+v]
#         if len(s)>=len(p) and int(s)<=int(p):
#             count += 1
#     return count

def solution(t, p):
    count = 0
    for v in range(len(t)):
        s=''
        if len(p)+v <= len(t):
            for i in range(v,len(p)+v):
                s += t[i]
            if s and int(s)<=int(p):
                count += 1
    return count