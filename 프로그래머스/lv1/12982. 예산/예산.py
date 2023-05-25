def solution(d, budget):
    count = 0
    money = 0
    d.sort()
    for i in d:
        money += i
        if money <= budget:
            count += 1
    return count