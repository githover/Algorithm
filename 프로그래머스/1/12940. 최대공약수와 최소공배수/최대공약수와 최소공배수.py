def solution(n, m):
    answer = []; gcd = []; lcm = []
    for i in range(1,n*m+1):
        if n % i == 0 and m % i == 0: #최대공약수
            gcd.append(i)
        if i % n == 0 and i % m == 0: #최소공배수
            lcm.append(i)
    answer.append(gcd[-1])
    answer.append(lcm[0])
    return answer