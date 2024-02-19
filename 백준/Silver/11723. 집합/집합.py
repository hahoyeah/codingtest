import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    command = input().strip().split()

    if command[0] == 'add':
        s.add(int(command[1]))
    elif command[0] == 'remove':
        s.discard(int(command[1]))  # discard 메서드는 없는 요소를 제거하려 해도 에러가 발생하지x
    elif command[0] == 'check':
        print(1 if int(command[1]) in s else 0)
    elif command[0] == 'toggle':
        if int(command[1]) in s:
            s.discard(int(command[1]))
        else:
            s.add(int(command[1]))
    elif command[0] == 'all':
        s = set(range(1, 21))  # 1부터 20까지 모든 수를 집합에 추가
    elif command[0] == 'empty':
        s = set()  # 집합을 비움
 