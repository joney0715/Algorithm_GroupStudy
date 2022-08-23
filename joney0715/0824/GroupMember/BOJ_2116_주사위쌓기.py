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

max_list = []
for i in range(6):
    idx_t = i
    result = 0
    result = max_value(dice_list[0], idx_t, result)
    for j in range(1,N):
        idx_b = dice_list[j].index(dice_list[j-1][idx_t])
        result = max_value(dice_list[j], idx_b, result)
        if idx_b == 0 or idx_b == 5:
            idx_t = abs(idx_b-5)
        if idx_b == 1 or idx_b == 2:
            idx_t = idx_b + 2
        if idx_b == 3 or idx_b == 4:
            idx_t = idx_b - 2
    max_list.append(result)  

answer = max(max_list)
print(answer)
