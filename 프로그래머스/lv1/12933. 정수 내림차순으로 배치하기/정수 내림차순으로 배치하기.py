def solution(n):
    a = sorted(list(map(str, str(n))),reverse=True)
    return int("".join(a))

# def solution(n):
#     a = sorted(list(str(n)),reverse=True)
#     return int("".join(a))

# def solution(n):
#     a = list(str(n))
#     a.sort(reverse = True)
#     return int("".join(a))