def solution(n, arr1, arr2):
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
