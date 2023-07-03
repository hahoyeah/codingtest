def solution(s):
    #queue로 풀자
    from collections import deque
    # from collections import Counter, defaultdict
    # a,b = Counter(s), defaultdict(int)
    x = len(s)
    q = deque(s)
    
    dic = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    result = 0

    for _ in range(x):
        stack = []
        for i in q:
            if stack and stack[0] in dic:
                break
            elif stack and i in dic and dic[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            result += 1
                
        ql = q.popleft()
        q.append(ql)
        
    return result