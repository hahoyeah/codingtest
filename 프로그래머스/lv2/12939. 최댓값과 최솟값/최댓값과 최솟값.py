def solution(s):
    ints = [int(i) for i in s.split()]
    return ' '.join([str(min(ints)),str(max(ints))])