def solution(cards1, cards2, goal):
    for i in goal:
        if cards1 and i in cards1:
            p = cards1.pop(0)
            if p != i:
                return "No"
            
        if cards2 and i in cards2:
            p = cards2.pop(0)  
            if p != i:
                return "No"
                
    return "Yes"

# def solution(cards1, cards2, goal):
#     for i in goal:
#         if len(cards1)>0 and i== cards1[0]:
#             cards1.pop(0)
            
#         elif cards2 and i== cards2[0]:
#             cards2.pop(0) 
#         else:
#             return "No"
                
#     return "Yes"