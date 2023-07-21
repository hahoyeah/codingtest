# import time #시간 계산하는 라이브러리
# start = time.time() #측정 시작

# import sys
# sys.setrecursionlimit(int(1e9))

# def solution(N, stages):
#     from collections import Counter,defaultdict
#     total = len(stages)
#     dic = Counter(stages)
#     result = defaultdict(int)
    
#     for i in range(1,N+1):
#         if dic[i]==0:
#             result[i]=0
#         result[i] = dic[i]/total
#         total -= dic[i]
    
#     result = sorted(result, key = lambda x:result[x], reverse=True)
    
#     return result

    # end = time.time()
    # print("time:" , end-start)

# def solution(N, stages):
#     from collections import Counter,deque
#     q = deque()
#     total = len(stages)
#     result = []
#     dic = Counter(stages)
#     fail = []
    
#     for i in range(1,N+1):
#         q.append([dic[i]/total,i])
#         fail.append(dic[i]/total)
#         total -= dic[i]
    
#     fail.sort()
    
#     while q:
#         p, ind = q.popleft()
#         if fail[-1] == p:
#             result.append(ind)
#             fail.pop()
#         else:
#             q.append([p,ind])
                
#     return result

def solution(N, stages):
    d = [0]*(N+2)
    total = len(stages)
    fail = []
    result=[]
    for i in stages:
        d[i] += 1
        
    for i in range(1,N+1):
        if d[i]==0:
            fail.append([i,0])
            continue
        fail.append([i,d[i]/total])
        total -= d[i]
    
    for i in sorted(fail, key = lambda x:(-x[1],x[0])):
        result.append(i[0])
    
    return result
