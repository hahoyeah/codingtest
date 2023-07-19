def solution(phone_number):
    return phone_number.replace(phone_number[:-4],"*"*len(phone_number[:-4]))

# def solution(phone_number):
#     return "*"*len(phone_number[:-4]) + phone_number[-4:]