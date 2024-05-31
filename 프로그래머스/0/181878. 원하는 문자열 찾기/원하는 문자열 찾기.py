def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    answer = int(pat in myString)
    return answer