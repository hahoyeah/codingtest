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
    
    # answer = s
    # for key, value in number.items(): #딕셔너리의 값과 키를 함께 사용할 수 있는 .items()를 꼭 기억하자!
    #     answer=answer.replace(key,str(value))
    # return int(answer)
    
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
        
            