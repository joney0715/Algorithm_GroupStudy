N, K = map(int, input().split())
C = list(map(int, input().split()))


added_temperature = 0
for i in range(K):
    added_temperature += C[i]
    # 지정된 일자 K만큼의 온도의 합을 구함

max_temperature = added_temperature
    #  초기 최대값 지정

for j in range(N-K):
    added_temperature -= C[j] - C[j + K]
    # 한 칸씩 진행

    if added_temperature >= max_temperature:
        max_temperature = added_temperature
    # 최대값 갱신



print(max_temperature)