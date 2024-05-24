def solution(myString, pat):
    string = ''
    for i in range(len(myString)):
        if myString[i] == 'A':
            string += 'B'
        else:
            string += 'A'
    return int(pat in string)