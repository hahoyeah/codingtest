import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
tree = list(map(int, input().split()))

def ans(n,m,tree):
    start = 0
    end = max(tree)
    result = 0

    while start<=end:
        total = 0
        mid = (start+end)//2

        if result==m:
            return result

        for i in tree:
            if i-mid>0:
                total+=i-mid

        if m<=total:
            result = max(result,mid)
            start = mid+1
        else:
            end = mid-1

    return result

print(ans(n,m,tree))