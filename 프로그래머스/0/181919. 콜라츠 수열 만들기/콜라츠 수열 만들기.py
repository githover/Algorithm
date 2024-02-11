def solution(n):
    answer = [n]
    for i in answer:
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3*i+1
        answer.append(i)
        if i == 1:
            break
    return answer