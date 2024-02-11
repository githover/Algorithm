def solution(num_list):
    mult = 1
    sum = 0
    answer = 0
    for i in num_list:
        mult *= i
        sum += i
    if mult < sum**2:
        return 1
    else:
        return 0