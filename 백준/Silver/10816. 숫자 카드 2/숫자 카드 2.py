import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import Counter

n = int(input())
s = list(map(int,input().split()))
m = int(input())
d = list(map(int,input().split()))

result = []

count = Counter(s)
for i in d:
    if i not in count:
        result.append(0)
    else:
        result.append(count[i])

print(" ".join(map(str,result)))