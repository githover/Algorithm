def solution(data, ext, val_ext, sort_by):
    answer = []
    column = ["code", "date", "maximum", "remain"]
    ext_idx = column.index(ext)
    sort_idx = column.index(sort_by)
    for i in range(len(data)):
        if data[i][ext_idx] < val_ext:
            answer.append(data[i])
    answer.sort(key=lambda x:x[sort_idx])
    
    return answer