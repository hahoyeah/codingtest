import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,k = map(int,input().split())
d = list(int(input().strip()) for _ in range(n))

result = 0
d.sort(reverse=True)

for i in d:
    if k >= i:
        result += k//i
        k = k%i

print(result)