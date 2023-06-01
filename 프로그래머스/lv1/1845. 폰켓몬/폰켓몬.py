def solution(nums):
    get = len(nums)/2
    if get > len(set(nums)):
        return len(set(nums))
    else:
        return get