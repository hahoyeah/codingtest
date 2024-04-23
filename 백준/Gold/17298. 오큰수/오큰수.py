import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

result = [-1]*n
stack = []

for i in range(n):
    while stack and d[i]>d[stack[-1]]:
        result[stack[-1]] = d[i]
        stack.pop()

    stack.append(i)
print(" ".join(map(str,result)))