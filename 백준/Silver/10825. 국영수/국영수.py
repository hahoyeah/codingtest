import sys
input = sys.stdin.readline

n = int(input())
d = []

for _ in range(n):
    dn = input().split()
    dn[1:] = map(int, dn[1:])
    d.append(dn)

d.sort(key = lambda v : (-v[1],v[2],-v[3],v[0]))

for i in d:
    print(i[0])