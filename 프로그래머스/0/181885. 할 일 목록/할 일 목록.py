def solution(todo_list, finished):
    answer = []
    a = list(zip(todo_list, finished))
    for i in range(len(a)):
        if a[i][1] == False:
            answer.append(a[i][0])
    return answer