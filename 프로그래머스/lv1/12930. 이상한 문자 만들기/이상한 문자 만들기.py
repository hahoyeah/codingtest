def solution(s):
    a=[]
    s=s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j%2==0:
                a.append(s[i][j].upper())
            else:
                a.append(s[i][j].lower())
        a.append(" ")

    c="".join(a[:-1])
    return c

#     k = s.split()    
#     ls= list(s)
#     answer = []
#     for i in k:
#         for j,v in enumerate(i):
#             if j == 0:
#                 answer.append(v.upper())
#             elif j % 2 == 0:
#                 answer.append(v.upper())
#             else:
#                 answer.append(v.lower())
#     for m in range(len(ls)):
#         if ls[m] == " ":
#             answer.insert(m," ") #insert는 리스트에
            
#     return "".join(answer)