def solution(rank, attendance):
    s=[]
    for i in range(len(rank)):
        if attendance[i] == True:
            s.append([i,rank[i]])
    s.sort(key = lambda x : x[1])
    return 10000*s[0][0] + 100*s[1][0] + s[2][0]