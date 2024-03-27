import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = input().strip()
s = input().strip()

ls = len(s)
count = 0
i = 0

while i <= (len(n)-ls):
    a = n[i:i+ls]
    if a == s:
        count += 1       
        i += ls
    else:
        i += 1

print(count)
