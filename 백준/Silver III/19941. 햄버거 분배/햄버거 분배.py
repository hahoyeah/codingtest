import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,k = map(int, input().split())
graph = list(input())

count = 0

for i in range(n):
    if graph[i]=='P':
        for j in range(max(i-k,0), min(i+k+1,n)):
            if graph[j] == 'H':
                count += 1
                graph[j]=0
                break

print(count)