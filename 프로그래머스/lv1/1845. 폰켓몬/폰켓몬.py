def solution(nums):
    return min(len(nums)/2, len(set(nums)))

    # if get > len(set(nums)):
    #     return len(set(nums))
    # else:
    #     return get