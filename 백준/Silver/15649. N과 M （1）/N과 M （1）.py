import sys
input = sys.stdin.readline

n,m = map(int,input().split())

def dfs(result):
    if len(result) == m:
        print(" ".join(map(str,result)))
        return

    for i in range(1,n+1):
        if i not in result:
            #result.append(i)
            dfs(result+[i])

dfs([])