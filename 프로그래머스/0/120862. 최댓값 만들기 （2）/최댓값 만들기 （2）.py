def solution(numbers):
    answer = 0
    mult_list = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            mult_list.append(numbers[i]*numbers[j])
    answer = max(mult_list)
    return answer