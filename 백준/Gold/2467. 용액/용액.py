import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))

total = 1e10
result = ''

start = 0
end = n-1

while start < end:
    if abs(d[start]+d[end]) < total:
        total = abs(d[start]+d[end])
        result = f'{str(d[start])} {str(d[end])}'

    if d[start]+d[end]<0:
        start += 1
        continue
    if d[start]+d[end]>0:
        end -= 1
        continue
    if d[start]+d[end]==0:
        result = f'{str(d[start])} {str(d[end])}'
        break

print(result)