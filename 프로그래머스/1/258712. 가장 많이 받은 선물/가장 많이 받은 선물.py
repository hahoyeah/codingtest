def solution(friends, gifts):
    answer = 0

    gift_map = {}
    giver_map = {}
    receiver_map = {}
    answer_map = {}

    # map에 friends를 등록함.
    for f1 in friends:
        inner_gift_map = {}
        for f2 in friends:
            if f1 == f2:
                continue
            inner_gift_map[f2] = 0
        gift_map[f1] = inner_gift_map
        answer_map[f1] = 0
        giver_map[f1] = 0
        receiver_map[f1] = 0

    # 선물에 대한 데이터를 Map에 저장함.
    for gift in gifts:
        giver, receiver = gift.split()
        gift_map[giver][receiver] += 1
        giver_map[giver] += 1
        receiver_map[receiver] += 1

    # 두 사람에 대한 조합을 지정해야 함.
    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            A = friends[i]
            B = friends[j]

            A_count = gift_map[A][B]
            B_count = gift_map[B][A]

            if A_count > B_count:
                answer_map[A] += 1
            elif B_count > A_count:
                answer_map[B] += 1
            else:
                A_value = giver_map[A] - receiver_map[A]
                B_value = giver_map[B] - receiver_map[B]

                if A_value > B_value:
                    answer_map[A] += 1
                elif B_value > A_value:
                    answer_map[B] += 1

    return max(answer_map.values())
    
#     from collections import Counter, defaultdict
    
#     dic = defaultdict(int)
#     count = defaultdict(int)
#     give = {}
#     get = {}
    
#     for i in friends:
#         give[i] = []
#         get[i] = []
    
#     for gift in gifts:
#         a, b = gift.split()
#         give[a].append(b)
#         get[b].append(a)
#         count[a] += 1
#         count[b] -= 1
    
#     for x in range(len(friends)-1):
#         for y in range(x+1,len(friends)):
#             k = friends[x]
#             v = friends[y]
#             ck = Counter(give[k])
#             cv = Counter(give[v])
#             if ck[v] > cv[k]: #k가 v한테 준 선물 개수 > v가 k한테 준 선물 개수
#                 dic[k] += 1
#             elif ck[v] < cv[k]:
#                 dic[v] += 1
#             else:
#                 if count[k] > count[v]:
#                     dic[k] += 1
#                 elif count[v] < count[k]:
#                     dic[v] += 1      
#                 else:
#                     continue
                        
#     return max(dic.values()) if dic else 0