# def solution(x):
#     k = list(str(x))
#     ha = 0
#     for i in k:
#         ha += int(i)
#     return x%ha == 0

def solution(x):
    ha = 0
    for i in str(x):
        ha += int(i)
    return x%ha == 0

# def solution(x):
#     return x%sum(int(x) for x in str(x)) == 0