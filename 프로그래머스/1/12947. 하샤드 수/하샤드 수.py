def solution(x):
    answer = True
    divideNum = sum([int(i) for i in str(x)])
    if x % divideNum != 0:
        answer = False
    return answer