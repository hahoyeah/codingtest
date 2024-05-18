# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

def dfs(n):
    visit = [[0]*n for _ in range(n)]
    r = [0,1,0,-1]
    c = [1,0,-1,0]
    k = 0
    a,b = 0,0
    count = 1
    visit[0][0]=1
    
    while count < n**2:
        nr = a+r[k]
        nc = b+c[k]
        if 0<=nr<n and 0<=nc<n and visit[nr][nc]==0:
            count += 1
            visit[nr][nc] = count
            a,b = nr,nc
        else:
            k = (k+1)%4
    return visit

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    result.append(dfs(n))

for i,v in enumerate(result):
    print(f'#{i+1}')
    for j in v:
        print(" ".join(map(str,j)))
        