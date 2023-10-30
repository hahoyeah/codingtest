import sys
input = sys.stdin.readline

from collections import deque
n = int(input())
d = list(map(int,input().split()))
result = []
q = deque(range(1,n+1))

while q:
    a = q.popleft()
    result.append(str(a))
    if not q:
        break
    if d[a-1]>0:
        for _ in range(d[a-1]-1):
            t = q.popleft()
            q.append(t)
    else:
        for _ in range(abs(d[a-1])):
            t = q.pop()
            q.appendleft(t)
            
print(' '.join(result))