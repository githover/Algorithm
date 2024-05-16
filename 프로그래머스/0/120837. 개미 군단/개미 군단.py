def solution(hp):
    first = hp // 5
    sec = (hp % 5) // 3
    third = (hp % 5) % 3
    answer = first + sec + third
    return answer