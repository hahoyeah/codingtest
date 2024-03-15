import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m,n = map(int, input().split())

for i in range(m,n+1):
    if i == 1:
        continue
    k = int(i**(1/2)) + 1
    for j in range(2,k):
        if i%j == 0:
            break
    else:
        print(i)