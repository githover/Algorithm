def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        num = ''    
        
        for j in range(s,len(i)):
            if j == s + l:
                break
            num += i[j]
        if int(num) > k:
            answer.append(int(num))
    return answer