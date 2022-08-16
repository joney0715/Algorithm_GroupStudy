# 주사위 옆면 중 최대값을 찾는 함수
def max_value(dice, idx, result):
    if idx == 0 or idx == 5:
        result += max(dice[1], dice[2], dice[3], dice[4])
    if idx == 1 or idx ==2:
        result += max(dice[idx-1], dice[idx+1], dice[idx+3], dice[(idx+4)%6])
    if idx == 3 or idx == 4:
        result += max(dice[idx-1], dice[idx-3], dice[idx+1], dice[(idx+2)%6])
    return result

N = int(input())

dice_list = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째 주사위의 윗면을 정하면 나머지 주사위는 자동으로 정해짐
# 첫 번째 주사위의 윗면에 올 숫자를 하나씩 처리
max_list = []
for i in range(6):
    # 첫 번째 주사위의 윗면 숫자
    idx_t = i

    # 옆면의 합
    result = 0

    # 첫 번쨰 주사위의 옆면중 가장 큰 숫자 검색
    result = max_value(dice_list[0], idx_t, result)

    # 쌓아올린 주사위 하나씩 처리
    for j in range(1,N):
        # 앞 주사위의 윗면과 같은 숫자를 검색해서 밑면으로 정의
        idx_b = dice_list[j].index(dice_list[j-1][idx_t])

        # 옆면 중 최대값 검색
        result = max_value(dice_list[j], idx_b, result)

        # 윗면 검색
        if idx_b == 0 or idx_b == 5:
            idx_t = abs(idx_b-5)
        if idx_b == 1 or idx_b == 2:
            idx_t = idx_b + 2
        if idx_b == 3 or idx_b == 4:
            idx_t = idx_b - 2
    max_list.append(result)  

# 모든 경우의 수(첫 번째 주사위의 윗면) 중
# 가장 큰 값 검색
answer = max(max_list)
print(answer)
