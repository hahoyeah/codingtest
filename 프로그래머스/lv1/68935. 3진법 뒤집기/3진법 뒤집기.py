def solution(n):
    k = 3
    s = ''
    result = 0
    while n:
        s += str(n%k)
        n=n//k
        
    return int(s,3)
    
    # for i,v in enumerate(s[::-1]):
    #     result += (3**i)*int(v)
    return result