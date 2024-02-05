import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

def k(n, d):

    result = []

    for i in range(n):
        count = 1

        for j in range(n):
            if d[i][0] < d[j][0] and d[i][1] < d[j][1]:
                count += 1

        result.append(str(count))

    return ' '.join(result)

print(k(n,graph))
