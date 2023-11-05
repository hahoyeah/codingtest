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
        q.rotate(-(d[a-1]-1))
    else:
        q.rotate(abs(d[a-1]))
            
print(' '.join(result))