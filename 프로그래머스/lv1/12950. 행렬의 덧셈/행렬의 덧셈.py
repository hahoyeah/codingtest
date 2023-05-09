def solution(arr1, arr2):
    answer =[]
        
    for i in range(len(arr1)):
        s = []
        for j in range(len(arr1[i])):
            s.append(arr1[i][j] + arr2[i][j])
        answer.append(s)    
    return answer
    
    #행과 열의 크기가 같기때문에 arr1[i]이렇게 굳이 안해도 돼
#     for i in range(len(arr1)):
#         for j in range(len(arr1[0])):
#             arr1[i][j] += arr2[i][j]
        
#     return arr1

    
    
