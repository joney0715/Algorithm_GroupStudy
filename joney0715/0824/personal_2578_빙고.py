import pprint
def find_bingo(bingo):
    cnt = 0
    for i in range(5):
        sum_row = sum_col = 0
        for j in range(5):
            sum_row += bingo[i][j]
            sum_col += bingo[j][i]
        if not sum_row:
            cnt += 1
        if not sum_col:
            cnt += 1

    sum_d1 = sum_d2 = 0
    for i in range(5):        
        sum_d1 += bingo[i][i]
        sum_d2 += bingo[i][-i-1]
    if not sum_d1:
        cnt += 1
    if not sum_d2:
        cnt += 1

    return cnt

bingo = [list(map(int, input().split())) for _ in range(5)]

N_list = []
for _ in range(5):
    N_list.extend(list(map(int, input().split())))

for i in range(25):
    flag = False
    for y in range(5):
        for x in range(5):
            if bingo[y][x] == N_list[i]:
                bingo[y][x] = 0
                flag = True
                break
        if flag:
            break
    
    if find_bingo(bingo) >= 3:
        print(i+1)
        break 
    

                