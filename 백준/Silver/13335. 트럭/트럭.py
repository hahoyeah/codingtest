import sys
input = sys.stdin.readline

from collections import deque
n,w,L = map(int,input().split())
d = list(map(int,input().split()))

result = 0
bridge = deque([0]*w)
cw = 0

for truck in d:
    while True:
        cw -= bridge.popleft()

        if sum(bridge) + truck <= L:
            bridge.append(truck)
            cw += truck
            result += 1
            break
        else:
            bridge.append(0)
            result +=1
result += w

print(result)