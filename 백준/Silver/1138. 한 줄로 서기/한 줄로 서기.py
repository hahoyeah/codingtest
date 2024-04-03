import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = list(map(int,input().split()))
d = [0]*n

for i in range(n):
    count = graph[i]
    for j in range(n):
        if d[j]==0 and count == 0:
            d[j]=i+1
            break
        elif d[j]==0: 
            count -= 1

print(' '.join(map(str,d)))