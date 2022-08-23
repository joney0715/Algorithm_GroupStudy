
for _ in range(4):
    x_1, y_1, p_1, q_1, x_2, y_2, p_2, q_2 = map(int, input().split())

    if p_1 < x_2 or p_2 < x_1: # 안 겹치는 경우
        x = 0
    if p_1 == x_2 or x_1 == p_2: # 점으로 만나는 경우
        x = 1
    if x_1 <= x_2 < p_1 or x_1 < p_2 <= p_1 or x_2 <= x_1 < p_2 or x_2 < p_1 <= p_2 : # 선으로 만나는 경우
        x = 2

    if q_1 < y_2 or q_2 < y_1: # 안 겹치는 경우
        y = 0
    if q_1 == y_2 or y_1 == q_2: # 점으로 만나는 경우
        y = 1
    if y_1 <= y_2 < q_1 or y_1 < q_2 <= q_1 or y_2 <= y_1 < q_2 or y_2 < q_1 <= q_2: # 선으로 만나는 경우
        y = 2

    if x == 0 or y == 0:
        print('d')
    elif x == 2 and y == 2:
        print('a')
    elif (x == 1 and y == 2) or (x == 2 and y == 1):
        print('b')
    elif x == 1 and y == 1:
        print('c')
