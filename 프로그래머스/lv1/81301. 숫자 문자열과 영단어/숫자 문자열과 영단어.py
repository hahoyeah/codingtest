def solution(s):
    number = {
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    }
    k=''
    result = ''
    for i in s:
        k+=i
        if k in number:
            result += str(number[k])
            k=''
        if i.isdigit():
            result += str(i)
            k=''
    return int(result)
        
            