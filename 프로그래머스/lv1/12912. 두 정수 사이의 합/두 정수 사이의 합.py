# def solution(a, b):
#     answer = 0
#     if a<b:
#         for i in range(a,b+1):
#             answer += i
#     elif a == b:
#         answer += a
#     else:
#         for i in range(b, a+1):
#             answer += i
#     return answer

def solution(a, b):
    answer = 0
    if a<b:
        answer = sum(range(a,b+1))
    else:
        answer = sum(range(b,a+1))
    return answer

# def solution(a, b):
#     if a>b:
#         a,b = b,a
#     return sum(range(a,b+1))