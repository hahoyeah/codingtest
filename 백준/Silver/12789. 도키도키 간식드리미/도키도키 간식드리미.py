# stack
import sys
input = sys.stdin.readline

n = input()
d = list(map(int,input().split()))

def result(d):
    stack = []
    first = 1 # 그다음 순서로 들어가야 할 번호
    for i in d:
        if i==first: # d의 맨 앞에 있는 값이 그다음 순서로 들어가야하는 번호이면 간식받는다
            first += 1 # 그리고 그 다음 순서를 기다린다
            while stack and stack[-1]==first: # 만약 쌓인 stack 맨 위에 다음 순서에 해당하는 번호가 있다면
                s = stack.pop() # 그 순서를 빼서 간식을 준다.
                first=s+1 # 그리고 그 다음 순서를 기다린다.
        else:
            stack.append(i) # 해당 안되는 것들은 stack넣는다

    return 'Nice' if not stack else 'Sad'
    # stack이 비어있으면 다 순서대로 간식을 받았다는 것이고 stack이 있다면 순서대로 간식을 받지못해 승환이 역시 받지 못했다.

print(result(d))