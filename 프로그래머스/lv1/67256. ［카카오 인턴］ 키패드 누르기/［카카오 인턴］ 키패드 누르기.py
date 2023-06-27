def solution(numbers, hand):
    left = 10 # * 시작부분
    right = 11 # # 시작부분
    result = ''
    dr = [-1,0,1,0]
    dl = [0,1,0,-1]
    a={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2],
      7:[2,0], 8:[2,1], 9:[2,2], 10:[3,0], 0:[3,1], 11:[3,2]}
    
    for k in numbers:
        if k == 1 or k==4 or k==7:
            result+='L'
            left = k
        elif k == 3 or k == 6 or k == 9:
            result+='R'
            right = k
        else:
            point = a[k]
            lp = a[left]
            rp = a[right]
            abs_rp = abs(rp[0]-point[0]) + abs(rp[1]-point[1]) 
            abs_lp = abs(lp[0]-point[0]) + abs(lp[1]-point[1])
            if abs_rp < abs_lp: #거리가 좁으면 더 가깝다. 값이 작을수록 더 가깝다
                result+='R'
                right = k
            elif abs_rp > abs_lp:
                result += 'L'
                left = k
            else:
                if hand == 'right':
                    result += 'R'
                    right = k
                else:
                    result += 'L'
                    left = k                    
            
            
    return result