import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = set(input() for _ in range(n))
d = []

for i in graph:
    d.append([len(i),i])

d.sort(key = lambda v : (v[0],v[1]))

for i,j in d:
    print(j.strip())