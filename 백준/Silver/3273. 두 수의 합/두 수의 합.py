import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
x = int(input())

count = 0
d.sort()
i = 0
j = n-1

while i < j:
    if d[i]+d[j]>x:
        j-=1
    elif d[i]+d[j]<x:
        i+=1
    else:
        count += 1
        i+=1
        j-=1

print(count)