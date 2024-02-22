import sys
input = sys.stdin.readline

n = int(input())
d = [input() for _ in range(n)]
s = []

for i in d:
    k = i.split()
    if 'push' in k[0]:
        s.append(int(k[1]))
    elif 'pop' == k[0]:
        if not s:
            print(-1)
        else:
            print(s.pop())
    elif 'size'==k[0]:
        print(len(s))
    elif 'empty'==k[0]:
        if not s:
            print(1)
        else:
            print(0)
    elif 'top'==k[0]:
        if not s:
            print(-1)
        else:
            print(s[-1])

