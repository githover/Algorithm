def solution(my_string, alp):
    for i in range(len(my_string)):
        up = my_string[i].upper()
        if my_string[i] == alp:
            my_string = my_string.replace(my_string[i],up)
    return my_string