import math
def solution(n):
    answer = 0
    for i in range(10000):
        if i*i == n:
            answer = 1
        else:
            continue
    if answer != 1:
        answer = 2
    return answer