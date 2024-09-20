def solution(picture, k):
    answer = []
    for i in picture:
        tmp = ''
        for j in i:
            tmp += k*j
        for l in range(k): 
            answer.append(tmp)
    return answer