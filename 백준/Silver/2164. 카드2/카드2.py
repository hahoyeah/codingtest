import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

q = deque(i for i in range(1,n+1))
count = 0

while len(q)>1:
    count += 1
    queue = q.popleft()
    if count%2==0:
        q.append(queue)

print(q[0])