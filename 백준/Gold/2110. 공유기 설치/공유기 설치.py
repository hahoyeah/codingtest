import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,c = map(int,input().split())
x = [int(input()) for _ in range(n)]
x.sort() # 정렬

# 거리
start = 1
end = x[-1] - x[0] # 가장큰 좌표에서 가장 작은 좌표의 거리

while start <= end:
    # 적정 중간 거리
    mid = (start+end) // 2
    current = x[0]
    count = 1

    for i in range(1,len(x)):
        if x[i]-current >= mid: # 두 좌표의 거리가 정한 거리보다 크거나 같으면
            count += 1 # 공유기 설치가 가능(가장 인접한 거리가 아니므로)
            current = x[i] # 큰 좌표값을 현재값으로 대체

    if count >= c: # 공유기를 더 많이 설치했기 때문에 거리를 늘려서 공유기를 줄여야한다
        start = mid+1 # 거리를 늘리기 위해
        result = mid # 가장 인접한 두 공유기 사이의 거리
    else:
        end = mid-1

# 최대 거리
print(result)