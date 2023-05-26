def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'*2
    up = 'DEFGHIJKLMNOPQRSTUVWXYZABC'*2
    result = ''
    for v in s:
        if v in low:
            li = low.find(f'{v}')
            result += low[li+n]
        elif v in up:
            ui = up.find(f'{v}')
            result += up[ui+n]  
        else:
            result += v
    return result