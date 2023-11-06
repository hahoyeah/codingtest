# stack
import sys
input = sys.stdin.readline

n = input()
d = list(map(int,input().split()))

def result(d):
    stack = []
    first = 1
    for i in d:
        if i==first:
            first += 1
            while stack and stack[-1]==first:
                s = stack.pop()
                first=s+1
        else:
            stack.append(i)

    return 'Nice' if not stack else 'Sad'

print(result(d))