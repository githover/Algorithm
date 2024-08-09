def solution(phone_number):
    phone_len = len(phone_number)
    answer = ['*' if i <= (phone_len-5) else phone_number[i] for i in range(phone_len)]
    answer = ''.join(answer)
    # answer = ''
    # for i in range(len(phone_number)):
    #     if i < len(phone_number)-4:
    #         answer += '*'
    #     else:
    #         answer += phone_number[i]
    return answer