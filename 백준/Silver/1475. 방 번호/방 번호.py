import sys
input = sys.stdin.readline

from collections import Counter

n = list(map(int,input().strip()))

def result(n):
    c=Counter(n)
    m = max(c.values())

    lis = []

    for key,v in c.items():
        if v == m:
            lis.append(key)

    if len(lis)==1:
        if lis[0]==6:
            if 9 not in c.keys():
                c[9]=0
            k = (c[6] - c[9])
            if k%2==0:
                return c[9] + k//2
            else:
                return c[9] + k//2 +1

        elif lis[0]==9:
            if 6 not in c.keys():
                c[6]=0
            k = (c[9] - c[6])
            if k%2==0:
                return c[6] + k//2
            else:
                return c[6] + k//2 +1
        else:
            return c[lis[0]]

    else:
        return m

print(result(n))