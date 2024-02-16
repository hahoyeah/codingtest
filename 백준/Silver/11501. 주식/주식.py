import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
result = []

def maxd(n, d):
    profit = 0
    max_price = d[-1]

    for i in range(n-2, -1, -1):
        if d[i] > max_price:
            max_price = d[i]
        else:
            profit += max_price - d[i]

    return profit

for _ in range(t):
    n = int(input())
    d = list(map(int,input().split()))

    result.append(maxd(n, d))
    
for k in result:
    print(k)
