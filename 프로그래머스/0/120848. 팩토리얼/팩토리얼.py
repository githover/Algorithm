def solution(n):
    answer = 0
    a = 1
    for i in range(1,n+1):
        a *= i
        if a <= n:
            # a *= i #넘어가기 전 시점이후에 곱하면 넘어가버림
            answer = i
        else:
            break
    return answer