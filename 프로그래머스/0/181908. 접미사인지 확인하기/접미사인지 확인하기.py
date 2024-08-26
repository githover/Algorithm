def solution(my_string, is_suffix):
    answer = 0
    idx = my_string.rfind(is_suffix)
    suf = len(my_string)-len(is_suffix)
    
    if idx == -1:
        answer = 0
    else:
        if idx == suf:
            answer = 1
        else:
            answer = 0
    return answer