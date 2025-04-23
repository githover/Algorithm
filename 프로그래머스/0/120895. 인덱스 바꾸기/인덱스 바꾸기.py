def solution(my_string, num1, num2):
    list_string = []
    new_string = ''
    for i in my_string:
        list_string.append(i)
    
    tmp = list_string[num1]
    list_string[num1] = list_string[num2]
    list_string[num2] = tmp
    
    for i in list_string:
        new_string += i
    
    return new_string