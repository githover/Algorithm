def solution(before, after):
    answer = 0
    bef_list = [i for i in before]
    aft_list = [i for i in after]
    answer = int(sorted(bef_list) == sorted(aft_list))
    return answer