import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from itertools import combinations, permutations

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

def total(team):
    t = 0
    for i,j in team:
        t += graph[i][j]
        t += graph[j][i]

    return t

def solution(n, graph):
    n2 = n//2
    com = list(combinations(range(n),n2))
    result = 1000

    for team1 in com:
        team2 = [i for i in range(n) if i not in team1]

        t1 = total(combinations(team1,2))
        t2 = total(combinations(team2,2))
        result = min(abs(t1-t2),result)

    return result

print(solution(n, graph))