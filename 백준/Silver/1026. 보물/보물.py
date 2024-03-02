import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

result = 0

a.sort()
b.sort(reverse=True)

for i,j in zip(a,b):
    result += i*j

print(result)