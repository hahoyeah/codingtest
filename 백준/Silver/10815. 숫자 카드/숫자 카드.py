import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

aa = set(a)
bb = set(b)

s = aa&bb
result = []

for i in b:
    if i in s:
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))