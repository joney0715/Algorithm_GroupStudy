# 빙고를 찾는 함수
def find_bingo(bingo):
    cnt = 0
    # 빙고의 행과 열 각각의 합을 구함
    for i in range(5):
        sum_row = sum_col = 0
        for j in range(5):
            sum_row += bingo[i][j]
            sum_col += bingo[j][i]
        if not sum_row:
            cnt += 1
        if not sum_col:
            cnt += 1
	
    # 대각선
    sum_d1 = sum_d2 = 0
    for i in range(5):        
        sum_d1 += bingo[i][i]
        sum_d2 += bingo[i][-i-1]
    if not sum_d1:
        cnt += 1
    if not sum_d2:
        cnt += 1

    return cnt

# 빙고 입력
bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부를 번호 입력
N_list = []
for _ in range(5):
    N_list.extend(list(map(int, input().split())))

# 사회자가 번호 하나씩 호출
for i in range(25):
    # 이중 반복문 break를 위한 flag
    flag = False
    # 빙고 중에 호출된 번호가 있는지 탐색
    for y in range(5):
        for x in range(5):
            # 빙고에 번호가 있는 경우
            if bingo[y][x] == N_list[i]:
                # 0으로 변환
                bingo[y][x] = 0
                flag = True
                break
        if flag:
            break
    
    # 빙고의 개수가 3 이상인 경우
    if find_bingo(bingo) >= 3:
        print(i+1)
        break 
    