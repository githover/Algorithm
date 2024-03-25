H, M = map(int,input().split())
if H == 0:
    if M >= 45:
        M = M - 45
    else:
        H = H + 23
        M = M + 15
else:
    if M >= 45:
        M = M - 45
    else:
        H = H - 1
        M = M + 15        
print(H, M)