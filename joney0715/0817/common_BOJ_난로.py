N, K = map(int, input().split())
t1 = int(input())

# 난로를 켜는 데 필요한 성냥 수
k_need = 1 
temp = []
# 난로가 켜진 시간
on_time = 1 

for _ in range(N-1):
    # 친구가 온 시간 입력
    t = int(input())
    # 친구가 오면 난로를 켜는 시간이 늘어남
    on_time += 1

    # 앞 친구가 온 시간과 비교해서 1타임 넘게 차이나면
    # 성냥을 새로 사용
    # 앞 친구와의 시간차 저장
    if t- t1 > 1:
        k_need += 1
        temp.append(t - t1 - 1)

    # 앞 친구 초기화
    t1 = t

# 시간차를 오름차순으로 정렬
temp.sort()

# 사용한 성냥이 가진 성냥 수와 같으면 정답 출력
if k_need <= K:
    print(on_time)
# 사용한 성냥이 가진 성냥을 초과하면
# 시간차가 적은 것은 난로를 끄지 않고 계속 켬
else:
    for i in range(k_need - K):
        on_time += temp[i]

    print(on_time)