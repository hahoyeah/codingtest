import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]

sett = set()

r = [0,1,0,-1]
c = [1,0,-1,0]

def s(i,j,result):
    if len(result) == 6:
        sett.add(result)
        return

    for k in range(4):
        dr = i + r[k]
        dc = j + c[k]
        if 0<=dr<5 and 0<=dc<5:
            s(dr,dc,result + str(graph[dr][dc]))

for i in range(5):
    for j in range(5):
        s(i,j,str(graph[i][j]))

print(len(sett))