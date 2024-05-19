# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

from collections import Counter

t = int(input())
for _ in range(t):
    num = int(input())
    d = list(map(int,input().split()))

    c = Counter(d)
    result = sorted(c.items(), key=lambda v: (-v[1],-v[0]))
    
    print(f'#{num} {result[0][0]}')