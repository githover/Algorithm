def solution(strArr):
    answer = 0
    len_list = []
    for i in strArr:
        len_list.append(len(i))
    max_count = 0
    for i in set(len_list):
        if len_list.count(i) >= max_count:
            max_count = len_list.count(i)
    
    return max_count