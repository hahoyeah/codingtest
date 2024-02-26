import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dn = set(input() for _ in range(n))
dm = set(input() for _ in range(m))
result = list(dn & dm)

print(len(result))
result.sort()
for i in result:
    print(i.strip())
