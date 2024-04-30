import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

result = []

while True:
    a = list(map(int, input().split()))
    if a==[0]:
        break
    k,s = a[0], a[1::]
    for i in range(k-5):
        for j in range(i+1,k-4):
            for b in range(j+1,k-3):
                for c in range(b+1,k-2):
                    for d in range(c+1,k-1):
                        for e in range(d+1,k):
                            result.append(f'{s[i]} {s[j]} {s[b]} {s[c]} {s[d]} {s[e]}')
    result.append(' ')

for ans in result:
    print(ans)