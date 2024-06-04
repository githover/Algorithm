def solution(myString):
    answer = []
    list = myString.split('x')
    for i in list:
        answer.append(len(i))
    return answer