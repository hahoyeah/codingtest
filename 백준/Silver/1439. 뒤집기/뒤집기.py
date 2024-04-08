import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

graph = input().strip()
d = [0,0]
k = ''

for i in graph:
    if not k:
        k+=i
        d[int(i)]+=1
    elif i != k:
        k = i
        d[int(i)]+=1

print(min(d))