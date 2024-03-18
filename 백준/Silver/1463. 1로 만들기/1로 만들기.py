import sys
input = sys.stdin.readline

n = int(input().strip())

d = [0] * 1000001

def s(n,d):
    if n == 1:
        return 0

    for i in range(2,n+1):
        if i%3==0 and i%2==0:
            d[i] = min(d[i//3],d[i//2],d[i-1]) + 1
        elif i % 3 == 0:
            d[i] = min(d[i//3],d[i-1]) + 1
        elif i % 2 == 0:
            d[i] = min(d[i//2],d[i-1]) + 1
        else:
            d[i] = d[i-1] + 1

    return d[n]

print(s(n,d))