def solution(people, limit):
    people.sort()
    left = 0
    right = len(people)-1
    result = 0
    
    while left<=right:
        if people[left]+people[right]>limit:
            right -= 1
            result += 1
        else:
            left += 1
            right -= 1
            result += 1
            
    return result