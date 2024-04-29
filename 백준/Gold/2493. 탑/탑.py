import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))

stack = []
result = []

for i in range(n):
    while True:
        if not stack:
            stack.append(i)
            result.append(0)
            break
        elif d[stack[-1]] < d[i]:
            stack.pop()
        elif d[stack[-1]] >= d[i]:
            result.append(stack[-1]+1)
            stack.append(i)
            break

print(" ".join(map(str,result)))