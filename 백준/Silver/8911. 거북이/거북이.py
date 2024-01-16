# F: 한 눈금 앞으로
# B: 한 눈금 뒤로
# L: 왼쪽으로 90도 회전
# R: 오른쪽으로 90도 회전

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [input() for i in range(n)]

dir = [[0,1],[1,0],[0,-1],[-1,0]]

for d in graph:
    # 시작점
    start = [0,0]

    # (x,y)
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    ds = 0

    for i in d:
        if i == 'F':
            start[0] += dir[ds][0]
            start[1] += dir[ds][1]
        elif i == 'B':
            b = (ds+2)%4
            start[0] += dir[b][0]
            start[1] += dir[b][1]            
        elif i == 'L':
            ds = (ds+3)%4
        else:
            ds = (ds+1)%4
        
        if max_x < start[0]:
            max_x=start[0]
        if max_y < start[1]:
            max_y=start[1]
        if min_x > start[0]:
            min_x=start[0]
        if min_y > start[1]:
            min_y=start[1]

    result = (max_x - min_x) * (max_y - min_y)
    print(result)