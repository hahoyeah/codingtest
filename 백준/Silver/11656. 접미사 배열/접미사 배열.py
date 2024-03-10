import sys
input = sys.stdin.readline

s = input().strip()

result = []

for i in range(len(s)):
    result.append(s[i:])

result.sort()
for k in result:
    print(k)