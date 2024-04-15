import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m,n = map(int,input().split())
graph = list(map(int,input().split()))

start = 1
end = max(graph)
result = 0

while start<=end:
    count = 0
    mid = (start+end)//2
    for i in graph:
        if i>=mid:
            count += i//mid
    if count >= m:
        start = mid+1
        result = max(result,mid)
    else:
        end = mid-1

print(result)