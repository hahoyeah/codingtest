import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]

d = d[::-1]
count = 20000
result = 0

for i in range(n):
    if d[i]>=count:
        result += d[i]-count+1
        d[i] = count-1
    
    count = d[i]

print(result)