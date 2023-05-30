def solution(a, b, n):
    s = 0 #남는거
    result = 0
    while n>=a:
        result += (n // a) * b
        n = (n // a) * b + n%a
    return result