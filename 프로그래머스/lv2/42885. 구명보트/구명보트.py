def solution(people, limit):
    #정렬한 뒤에 왼쪽 오른쪽을 더해서
    #limit보다 크면 맨 오른쪽은 혼자태움
    #그 다음으로 덜뚱뚱한 사람으로 비교
    result = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] > limit:
            result += 1
            right -= 1
        else:
            result += 1
            left += 1
            right -= 1
    return result
            
        