
def gasstation(gas, cost):
    # 연료 총합과 코스트 총합을 비교해서 불가능한 경우를 제외
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발 안되는 지점
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    
    return start

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

answer = gasstation(gas, cost)
print(answer)