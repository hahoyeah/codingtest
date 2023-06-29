def solution(queue1, queue2):
    from collections import deque
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    sum_s = sum(queue1) + sum(queue2)
    if sum_s % 2 != 0:
        return -1
    s = (sum_s)//2
    s1 = sum(queue1)
    s2 = sum(queue2)
    # sum을 해주면 시간이 오래걸리니까 최대한 while문에서 
    # sum이 반복되지 않게 하기
    limit = len(queue1)*2
    p1,p2 = 0,0
    while p1 < limit and p2 < limit:
        if s1 > s:
            q = queue1.popleft()
            queue2.append(q)
            s1 -= q
            s2 += q
            p1 += 1
        elif s2 > s:
            q = queue2.popleft()
            queue1.append(q)
            s1 += q
            s2 -= q
            p2 += 1
        else:
            return p1+p2
    return -1