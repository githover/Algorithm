def solution(s):
    s = s.lower()
    p_count = s.count('p')
    y_count = s.count('y')
    if p_count == y_count:
        if p_count == 0 and y_count == 0:
            return True
        return True
    else:
        return False
    