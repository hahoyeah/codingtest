def solution(n, arr1, arr2):
    # answer = []
    # for i,j in zip(arr1,arr2):
    #     arr12 = str(bin(i|j)[2:]) #str안써도 이미 str
    #     arr12 = arr12.rjust(n,'0')
    #     arr12 = arr12.replace('1','#')
    #     arr12 = arr12.replace('0',' ')
    #     answer.append(arr12)
    # return answer
    
    result = []
    for i,j in zip(arr1,arr2):
        arr1_bb = ''
        arr2_bb = ''
        s = ''
        arr1_b = bin(i)[2:] #arr1_b = format(i, 'b')
        arr2_b = bin(j)[2:]
        arr1_bb += '0'*(n-len(arr1_b)) + arr1_b
        arr2_bb += '0'*(n-len(arr2_b)) + arr2_b
        for v,k in zip(arr1_bb,arr2_bb):
            if v=='0' and k=='0':
                s += ' '
            else:
                s += '#'
        result.append(s)
    
    return result


