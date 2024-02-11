def solution(num_list):
    result = []
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result.append(len(even))
    result.append(len(odd))
    return result