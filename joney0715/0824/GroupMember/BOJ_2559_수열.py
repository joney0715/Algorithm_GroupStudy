
N, K = map(int, input().split())

temp = list(map(int, input().split()))

sum_value = 0
for i in range(K):
    sum_value += temp[i]

max_value = sum_value
j = 0
while j+K < N:
    sum_value = sum_value - temp[j] + temp[K+j]
    if max_value < sum_value:
        max_value = sum_value
    j += 1
print(max_value)