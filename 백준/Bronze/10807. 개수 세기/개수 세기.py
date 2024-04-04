N = int(input())
num_list = list(map(int,input().split()))
v = int(input())
sum = 0
for i in range(0,N):
    if v == num_list[i]:
        sum += 1
print(sum)