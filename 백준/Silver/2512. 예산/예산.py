import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
total = int(input())

start = 0
end = max(budget)

while start<=end:
    result = 0
    mid = (start+end)//2 # 절반을 기점(상한액으로 지정)
    for i in budget:
        if i <= mid: # 상한액보다 작으면
            result += i
        else:
            result += mid
    if total >= result:
        start = mid+1 # 시작을 절반+1로 높인다
        answer = mid # 가능한 한 최대의 총 예산
    else:
        end = mid-1 # 끝을 절반-1로 줄인다

print(answer)