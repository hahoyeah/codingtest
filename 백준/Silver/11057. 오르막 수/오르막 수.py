import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

# n-1
d = [[1]*10 for _ in range(n)]

# 행
for i in range(1,n):
    # 열
    for j in range(1,10):
        d[i][j] = d[i][j-1]+d[i-1][j]

print(sum(d[n-1])%10007)