def solution(n):
    answer = 0
    for i in range(1,len(str(n))+1):
        if i == 1:
            answer += n % 10**i
        elif i == len(str(n)):
            answer += n // 10**(i-1)
        else:
            answer += (n % 10**i) // 10**(i-1)
    # n_str = str(n)
    # for i in n_str:
    #     answer += int(i)
    return answer