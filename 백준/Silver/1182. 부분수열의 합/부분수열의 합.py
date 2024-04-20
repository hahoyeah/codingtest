import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from itertools import permutations, combinations

n,s = map(int,input().split())
d = list(map(int,input().split()))

count = 0

for i in range(1,n+1):
    comb = combinations(d,i)
    for j in comb:
        if s == sum(j):
            count += 1

print(count)