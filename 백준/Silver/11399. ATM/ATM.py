n = int(input())
p = list(map(int, input().split()))

p.sort()
t = 0
total = 0

for i in p:
    t += i
    total += t
    
print(total)