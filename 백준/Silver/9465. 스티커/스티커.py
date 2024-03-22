import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
result = []
for i in range(n):
    m = int(input())
    graph = [list(map(int,input().split())) for _ in range(2)]

    d = [[0] * m for _ in range(2)]

    r = [1,1,-1,-1]
    c = [1,2,1,2]
    d[0][0] = graph[0][0]
    d[1][0] = graph[1][0]

    # 대각선과 대각선 옆을 선택 둘 중 하나
    # 첫째줄부터 시작할지 두번째부터 시작할지
    for k in range(m):
        if k == m-1:
            result.append(max(d[0][m-1],d[1][m-1]))

        for i in range(2):
            dr = 0+r[i]
            dc = k+c[i]
            if 0<=dc<m:
                d[dr][dc] = max(d[dr][dc],graph[dr][dc]+d[0][k])

        for i in range(2,4):
            dr = 1+r[i]
            dc = k+c[i]
            if 0<=dc<m:
                d[dr][dc] = max(d[dr][dc],graph[dr][dc]+d[1][k])

for k in result:
    print(k)