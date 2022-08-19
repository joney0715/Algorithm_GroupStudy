T = int(input())

list0 = [0]*41
list0[0] = 1
for i in range(2,41):
    list0[i] = list0[i-1] + list0[i-2]

list1 = [0]*41
list1[1] = 1
for i in range(2,41):
    list1[i] = list1[i-1] + list1[i-2]

# 피보나치 수열 리스트 작성

for _ in range(T):
    N = int(input())
    print (list0[N], list1[N])