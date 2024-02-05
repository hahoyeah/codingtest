import sys
input = sys.stdin.readline

dic = {'Y':1, 'F':2,'O':3}

n, a = input().split()
k = dic[a]

g = [input() for _ in range(int(n))]
graph = set(g)

print(len(graph)//k)