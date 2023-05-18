# def solution(n):
#     x=0
#     for i in range(1,n):
#         if n % i == 1:
#             x += i
#             break
#     return x

def solution(n):
    x=[]
    for i in range(1,n):
        if n % i == 1:
            x.append(i)

    return x[0]

# def solution(n):
#     return [x for x in range(1,n) if n % x == 1][0]

    
####출력테스트
# print(solution(10))
# print(solution(12))