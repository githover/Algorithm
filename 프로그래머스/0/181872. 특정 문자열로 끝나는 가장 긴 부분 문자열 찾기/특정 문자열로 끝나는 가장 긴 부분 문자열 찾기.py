def solution(myString, pat):
    index = myString.rfind(pat)
    answer = myString[0:index+len(pat)]
    return answer