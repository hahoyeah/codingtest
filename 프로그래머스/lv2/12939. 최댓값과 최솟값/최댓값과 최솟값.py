def solution(s):
    #ints = list(map(int,s.split()))
    ints = [int(i) for i in s.split()]
    return ' '.join([str(min(ints)),str(max(ints))])