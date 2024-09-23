def solution(numer1, denom1, numer2, denom2):
    gcd = 1
    for i in range(1, min(denom1,denom2)+1): # 최대공약수
        if denom1 % i == 0 and denom2 % i == 0:
            gcd = i
    lcm = denom1 * denom2 // gcd # 최소공배수
    mult1 = lcm // denom1; mult2 = lcm // denom2
    bunmo = (numer1 * mult1) + (numer2 * mult2)
    tmp = 0
    for i in range(1,min(bunmo,lcm)+1): # 기약분수 만들기
        if bunmo % i == 0 and lcm % i == 0:
            tmp = i
    bunmo = bunmo // tmp
    lcm = lcm // tmp
    answer = [bunmo, lcm]
    return answer