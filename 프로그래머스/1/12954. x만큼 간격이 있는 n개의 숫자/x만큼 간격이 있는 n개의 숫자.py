def solution(x, n):
    answer = []
    d = x
    for i in range(1,n+1):
        answer.append(x)
        x += d
    return answer