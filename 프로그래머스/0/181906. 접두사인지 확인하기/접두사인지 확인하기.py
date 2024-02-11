def solution(my_string, is_prefix):
    answer = 0
    pref_list = []
    for i in range(len(my_string)):
        pref_list.append(my_string[:i])  
    if is_prefix in pref_list:
        answer = 1
    else:
        answer = 0
    return answer