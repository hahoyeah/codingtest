def solution(cap, n, deliveries, pickups):
    deliver = deliveries[::-1]
    pick = pickups[::-1]
    
    answer = 0
    d = 0
    p = 0
    
    for i in range(n):
        d += deliver[i]
        p += pick[i]
        
        while d >0 or p >0:
            d -= cap
            p -= cap
            answer += (n-i)*2
            
    return answer