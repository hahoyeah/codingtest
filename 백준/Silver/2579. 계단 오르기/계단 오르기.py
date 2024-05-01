import sys
input = sys.stdin.readline

n = int(input())
step = [int(input()) for _ in range(n)]

def ans(n,step):

    d = [0]*(n+1)

    if n < 3:
        return sum(step)

    d[1] = step[0]
    d[2] = d[1] + step[1]

    for i in range(3,n+1):
        d[i] = max(d[i-2]+step[i-1], d[i-3]+step[i-2]+step[i-1]) # step[i-1]는 d[i]의 인덱스와 동일

    return d[n]

print(ans(n,step))