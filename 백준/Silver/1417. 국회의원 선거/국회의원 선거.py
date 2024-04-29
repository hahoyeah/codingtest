import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
d = [int(input().strip()) for _ in range(n)]

def ans(n,d):
    if n==1:
        return 0

    my = d[0]
    d = d[1::]
    d.sort()
    result = 0

    while my <= d[-1]:
        result += 1
        d[-1]-=1
        my+=1
        d.sort()
    return result

print(ans(n,d))