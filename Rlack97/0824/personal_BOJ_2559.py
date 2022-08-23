N, K = map(int, input().split())
C = list(map(int, input().split()))


added_temperature = 0
for i in range(K):
    added_temperature += C[i]

max_temperature = added_temperature

for j in range(N-K):
    added_temperature -= C[j] - C[j + K]

    if added_temperature >= max_temperature:
        max_temperature = added_temperature



print(max_temperature)