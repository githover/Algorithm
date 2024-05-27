def solution(arr):
    answer = []
    for i in arr:
        for j in range(int(i)):
            answer.append(i)
    return answer