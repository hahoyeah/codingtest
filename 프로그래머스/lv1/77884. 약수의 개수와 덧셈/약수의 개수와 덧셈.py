def solution(left, right):
    count = [0]*(right-left+1)
    result = 0
    for i,k in zip(range(left,right+1),range(right-left+1)):
        for j in range(1,right+1):
            if i % j == 0 and i >= j:
                count[k] += 1
        if count[k] % 2 == 0:
            result += i
        else:
            result -= i
    return result 

# 와 미쳐따...루트 씌어서 즉 x**2 = y가 되면 이건 약수의 개수가 홀수야

# def solution(left, right):
#     result = 0
#     for i in range(left,right+1):
#         if i**0.5 == int(i**0.5): #홀수면 정수로 나누어 떨어져
#             result -= i
#         else:
#             result += i
#     return result

# import math
# def solution(left, right):
#     result = 0
#     for i in range(left,right+1):
#         if math.sqrt(i) == int(math.sqrt(i)): #홀수면 정수로 나누어 떨어져
#             result -= i
#         else:
#             result += i
#     return result  