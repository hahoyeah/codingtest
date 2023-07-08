def solution(rank, attendance):
    s = []
    for i,j in zip(range(len(rank)), attendance):
        if j == True:
            s.append((rank[i], i))
    s.sort(key = lambda x:x[0])        
    
    return s[0][1]*10000 + s[1][1]*100 + s[2][1]
    
    