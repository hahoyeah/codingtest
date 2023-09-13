a = int(input())

d = [0]*(a+2)
d[1]=1
d[2]=2

if a>2:
    for i in range(3,a+1):
        d[i] = (d[i-1]+d[i-2])%15746
        
print(d[a])

# 메모리 초과...
        