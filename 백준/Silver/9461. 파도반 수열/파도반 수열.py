import sys

n = int(sys.stdin.readline())
k = [int(sys.stdin.readline().strip()) for _ in range(n)]

d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1

if max(k)>3:
    for i in range(4,max(k)+1):
        d[i] = d[i-2]+d[i-3]

for j in k:
    print(d[j])