def solution(num_list):
    odd=''
    even=''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            odd += str(num_list[i])
            print(odd)
        else:
            even += str(num_list[i])
            print(even)
    return int(odd)+int(even)