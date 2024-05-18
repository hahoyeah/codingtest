# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.


#import sys
#sys.stdin = open(&quot;input.txt&quot;, &quot;r&quot;)

ans = []
for _ in range(1,11):
    n = int(input())
    d = list(map(int,input().split()))
    
    result = 0
    i = 2
    while i<(n-2):
        k = max(d[i-2],d[i-1],d[i+1],d[i+2])
        if k < d[i]:
            result += d[i]-k
            i += 3
        else:
            i += 1
    ans.append(result)

for s in range(1,11):
    print(f'#{s} {ans[s-1]}')
       
