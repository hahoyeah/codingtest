import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]
stack = []

for i in d:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack) if stack else 0)