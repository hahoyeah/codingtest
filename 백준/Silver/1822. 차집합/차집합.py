import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

s = a-b
print(len(s))

if s:
    result = list(s)
    result.sort()
    result = list(map(str,result))
    print(" ".join(result))