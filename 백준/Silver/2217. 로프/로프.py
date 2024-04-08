import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
w = [int(input()) for _ in range(n)]

w.sort(reverse=True)
result = 0

while n>0:
    result = max(result,w[-1]*n)
    w.pop()
    n-=1

print(result)