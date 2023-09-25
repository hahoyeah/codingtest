s = input()

number = s.split('-')
number = '+'.join(number).split('+')
code = []

total = int(number[0])
for i in s:
    if i == '-' or i == '+':
        code.append(i)
       
k = 0
while k < len(code):
    if code[k]=='-':
        while k < len(code):
            total -= int(number[k+1])
            k += 1  
    else:
        total += int(number[k+1])
        k += 1        
        
print(total)