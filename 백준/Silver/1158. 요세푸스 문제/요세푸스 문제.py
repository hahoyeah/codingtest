import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

n,k = map(int,input().split())

queue = deque(range(1,n+1))
result = []

while queue:
    for _ in range(k-1):
        q = queue.popleft()
        queue.append(q)
    q = queue.popleft()
    result.append(q)

ans = ', '.join(map(str,result))
print(f'<{ans}>')