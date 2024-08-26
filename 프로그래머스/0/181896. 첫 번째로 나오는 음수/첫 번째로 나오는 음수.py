def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        idx = num_list.index(num_list[i])
        if num_list[i] < 0:
            answer = idx
            break
        answer = -1
    return answer