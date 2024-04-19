import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

n,k = map(int,input().split())

def bfs(n,k):
    visit = [0]*100001
    queue = deque()
    queue.append(n)
    count = 0

    while queue:
        count += 1
        for _ in range(len(queue)):
            q = queue.popleft()
            if q == k:
                return count
            if 0<=q<=100000 and visit[q]==0:
                visit[q]=1
                queue.append(q+1)
                queue.append(q-1)
                queue.append(2*q)

print(bfs(n,k)-1)