def solution(a, b):
    #윤년은 2월 29일 포함
    dic = {
        6:'SUN',
        0:'MON',
        1:'TUE',
        2:'WED',
        3:'THU',
        4:'FRI',
        5:'SAT'
    }
    import datetime as dt
    a = dt.datetime(2016,a,b)
    return dic[a.weekday()]
    
    # week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    # end = [31,29,31,30,31,30,31,31,30,31,30,31]
    # return week[(sum(end[:a-1]) + b -1)%7]