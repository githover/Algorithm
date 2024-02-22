def solution(num, k):
    try:
        result = str(num).index(str(k))+1
    except:
        result = -1
    return result
    