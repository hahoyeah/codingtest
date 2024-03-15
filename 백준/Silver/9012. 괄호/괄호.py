import sys
input = sys.stdin.readline

n = int(input())
a = [input().strip() for _ in range(n)]

for k in a:
    stack = []
    for i in k:
        if stack and i==')' and '('==stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        print('NO')
    else:
        print('YES')