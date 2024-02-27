import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for _ in range(n)]

d = [0] * 12

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(3,11):
    d[i+1] = d[i]+d[i-1]+d[i-2]

for i in graph:
    print(d[i])