def solution(s):
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y += 1
    return p == y

# def solution(s):
#     return s.lower().count('p') == s.lower().count('y') #lower로 소문자로 다 바꿔준 후에 카운트

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( solution("pPoooyY") )
# print( solution("Pyy") )