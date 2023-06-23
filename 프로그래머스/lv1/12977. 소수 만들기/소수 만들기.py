import itertools
from itertools import combinations as cb #cb(n,k)=itertools.combinations(n,k)
# itertools.combinations(n,k)은 순서상관없이 n개중에서 서로다른 k개 선택(조합)
# permutations은 순서상관있음!(순열)

def solution(nums):
    result = len(list(itertools.combinations(nums,3)))
    for i in list(cb(nums,3)):
        s = sum(i)
        for v in range(2,s): #int(s**0.5) + 1
            if s % v == 0:
                result -= 1
                break
    return result

# 서로 다른 3개... 종복x