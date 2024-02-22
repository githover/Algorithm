def solution(num, k):
    result = str(num).find(str(k))+1
    if result == 0:
        result = -1
    return result
    