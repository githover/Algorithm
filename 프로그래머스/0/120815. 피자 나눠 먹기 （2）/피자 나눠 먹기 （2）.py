def solution(n):
    answer = 0
    a = 0
    while True:
        a += 1
        if (a*6) % n == 0:
            answer = a
            break
        
    return answer