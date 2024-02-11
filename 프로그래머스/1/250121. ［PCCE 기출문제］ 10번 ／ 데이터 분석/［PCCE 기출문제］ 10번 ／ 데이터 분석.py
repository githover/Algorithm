def solution(data, ext, val_ext, sort_by):
    answer = []
    for i in range(len(data)):
        if ext == "code":
            if data[i][0] < val_ext:
                answer+=[data[i]]
        elif ext == "date":
            if data[i][1] < val_ext:
                answer+=[data[i]]
        elif ext == "maximum":
            if data[i][2] < val_ext:
                answer+=[data[i]]
        elif ext == "remain":
            if data[i][3] < val_ext:
                answer+=[data[i]]
    if sort_by == "code":
        answer.sort(key=lambda x: x[0])
    elif sort_by == "date":
        answer.sort(key=lambda x: x[1])
    elif sort_by == "maximum":
        answer.sort(key=lambda x: x[2])
    elif sort_by == "remain":
        answer.sort(key=lambda x: x[3])
    return answer