import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

import heapq

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]

queue = []
result = []

for i in d:
    if not queue and i == [0]:
        result.append(-1)
    elif i != [0]:
        k = i[0]
        for j in range(1,k+1):
            heapq.heappush(queue,-i[j])
    elif i==[0]:
        h = heapq.heappop(queue)
        result.append(-h)

for ans in result:
    print(ans)