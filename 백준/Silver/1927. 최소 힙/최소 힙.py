import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

heap = []

for i in x:
    if i == 0:
        if not heap:
            print(0)
        else:
            h = heapq.heappop(heap)
            print(h)

    else:
        heapq.heappush(heap,i)