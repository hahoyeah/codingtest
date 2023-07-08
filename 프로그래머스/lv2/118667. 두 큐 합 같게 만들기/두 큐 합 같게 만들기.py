def solution(queue1, queue2):
    from collections import deque
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)
    
    if (s1+s2)%2==1:
        return -1
    
    p1,p2 = 0,0
    limit = len(q1)*2
    while q1 and q2 and p1<limit and p2<limit:
        if s1>s2:
            q = q1.popleft()
            q2.append(q)
            s1 -= q
            s2 += q
            p1 += 1
        elif s1<s2:
            q = q2.popleft()
            q1.append(q)
            s2 -= q
            s1 += q
            p2 += 1      
        else:
            return p1+p2
    
    return -1
        