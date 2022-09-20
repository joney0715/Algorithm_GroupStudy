
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

answer = -1
# 시작점
for start in range(len(gas)):
    fuel = 0
    # 시작점에서 한 바퀴 돌기
    for i in range(start, len(gas) + start):
        # 인덱스에 맞게 변환
        idx = i % len(gas)

        # 이동 가능 여부
        can_travel = True
        # 기존의 연료에 충전해도 못가는 경우
        if gas[idx] + fuel < cost[idx]:
            can_travel = False
            break
        # 갈 수 있는 경우
        else:
            fuel += gas[idx] - cost[idx]
    
    # 처리가 끝난 후 이동이 가능한 경우
    if can_travel:
        answer = start

print(answer)