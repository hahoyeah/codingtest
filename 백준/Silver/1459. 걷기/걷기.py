import sys
input = sys.stdin.readline

x,y,w,s = map(int,input().split())

if 2*w >= s: # 대각선으로만 이동, 대각선 + 평행
    if w>s:
        m1 = min(x,y)*s + (abs(x-y)//2)*2*s + (abs(x-y)%2)*w
    else:
        m1 = min(x,y)*s + abs(x-y)*w
else:
    m1 = (x+y)*w

print(m1)