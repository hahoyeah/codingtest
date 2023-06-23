# def solution(n):
#     answer = 0
#     for i in range(2,n+1):
#         for j in range(2,int(i**0.5)+1):
#             if i%j == 0:
#                 break
#         else:
#             answer += 1
#     return answer


def solution(n):
    # set은 중복제거 및 순서 정렬
    num = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(i*2, n+1, i))
            
    return len(num)