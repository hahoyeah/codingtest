def solution(n):
    answer = list(map(int, str(n))) # int를 반복하면 오류가 나므로 str로 바꿔준 후 매개변수 함수인 int를 적용시켜준다.
    # map(적용시킬 함수, 적용할 값들)
    return sum(answer)

# def solution(n):
#     return sum([int(i) for i in str(n)])
