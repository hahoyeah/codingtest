def solution(friends, gifts):
    from collections import defaultdict
    count = {s:0 for s in friends}
    # 준 개수
    give_count = {s:defaultdict(int) for s in friends}
    
    # 받은 개수
    send_count = {s:defaultdict(int) for s in friends}
    
    for i in gifts:
        give, send = i.split()
        # 준 개수
        give_count[give][send] += 1
        # 받은 개수
        send_count[send][give] += 1
    
    t = []
    for i in friends:
        for j in friends:
            t.append(i)
            if j not in t:
                ij = give_count[i][j]
                ji = give_count[j][i]
                if ij > ji:
                    count[i] += 1
                elif ij < ji:
                    count[j] += 1
                else:
                    a = sum(give_count[i].values()) - sum(send_count[i].values())
                    b = sum(give_count[j].values()) - sum(send_count[j].values())
                    if a > b:
                        count[i] += 1
                    elif a < b:
                        count[j] += 1
    return max(count.values())
    
    