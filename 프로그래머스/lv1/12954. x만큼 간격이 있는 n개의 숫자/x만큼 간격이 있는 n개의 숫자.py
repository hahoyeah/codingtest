def solution(x, n):
    result = []
    for i in range(1, n+1):
        result.append(x * i)
    return result

# def solution(x, n):
#     return [i * x + x for i in range(n)]