def solution(n):
    sqrt = n**(1/2)
    if int(sqrt) == sqrt: # sqrt % 1 == 0
        return int((sqrt+1)**2)
    else:
        return -1

#print(solution(121))
#print(solution(3))
