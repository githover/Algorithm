def solution(arr):
    answer = []
    min_val = 1000
    if len(arr) <= 1:
        answer.append(-1)
    else:
        for i in range(len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
        arr.remove(min_val)
        answer = arr
    return answer