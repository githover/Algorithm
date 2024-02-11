def solution(my_string, letter):
    for i in my_string:
        if i == letter:
            my_string = my_string.replace(letter,'')    

    return my_string