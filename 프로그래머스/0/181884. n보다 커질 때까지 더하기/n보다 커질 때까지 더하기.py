def solution(numbers, n):
    sum = 0
    for i in numbers:
        num = 0
        num += i
        sum += num
        if sum > n: 
            break
    return sum