def solution(money):
    answer = []
    num = money // 5500
    remain = money - 5500*num
    answer.append(num)
    answer.append(remain)
    return answer