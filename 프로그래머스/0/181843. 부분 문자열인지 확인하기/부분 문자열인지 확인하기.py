def solution(my_string, target):
    answer = my_string.find(target)
    if answer >= 0:
        return 1
    else:
        return 0