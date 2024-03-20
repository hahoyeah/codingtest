import sys
input = sys.stdin.readline

k, n = map(int, input().split())
d = [int(input()) for _ in range(k)]

def ans(k,n,d):
    start = 1
    end = max(d)
    len = 0

    while start<=end:
        result = 0

        mid = (start+end)//2
        for i in d:
            result += i // mid

        if result >= n:
            start = mid + 1
            len = max(mid, len)
        if result < n:
            end = mid - 1

    return len

print(ans(k,n,d))