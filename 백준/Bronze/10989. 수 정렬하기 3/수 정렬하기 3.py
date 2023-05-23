import sys
input = sys.stdin.readline

n= int(input())
count = [0]*(10_000+1) #0도 자연수에 포함하기 때문에 1을 더해주는 듯?(문의)
for _ in range(n):
    count[int(input())] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i) #오름차순으로, count의 인덱스는 수, 값은 개수
        