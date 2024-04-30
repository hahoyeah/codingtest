import sys
input = sys.stdin.readline

n,m = map(int,input().split())

def dfs(result,k):
    if len(result) == m:
        print(" ".join(map(str,result)))
        return

    for i in range(k,n+1):
        dfs(result+[i],i+1)

dfs([],1)