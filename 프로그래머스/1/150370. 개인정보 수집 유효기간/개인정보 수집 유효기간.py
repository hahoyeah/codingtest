def solution(today, terms, privacies):
    from datetime import datetime, timedelta
    y,m,d = map(int,today.split("."))
    current = datetime(y,m,d)
    answer = []
    
    t = {}
    for i in terms:
        al,num = i.split()
        t[al] = int(num)
        
    for i,j in enumerate(privacies):
        day, k = j.split()
        a,b,c = map(int, day.split('.'))
        year = a + (b+t[k]-1)//12
        month = (b+t[k]-1)%12+1
        days = c
            
        if days-1 == 0:
            if month == 1:
                end = datetime(year-1,12,28)
            else:
                end = datetime(year,month-1,28)
        else:
            end = datetime(year,month,days-1)
        
        if current > end:
            answer.append(i+1)
            
    return answer
        