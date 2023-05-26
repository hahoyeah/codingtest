def solution(sizes):
    mi, ma = [], []
    for i in sizes:
        mi.append(min(i))
        ma.append(max(i))
    return max(ma) * max(mi)
            