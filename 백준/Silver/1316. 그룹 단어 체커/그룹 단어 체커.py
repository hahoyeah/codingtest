import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
a = [input() for _ in range(n)]

result = 0

for i in a:
    d = []
    for k in i:
        if not d or k not in d:
            d.append(k)
            end = k
        elif k == end:
            continue
        elif k in d:
            break
    else:
        result += 1

print(result)