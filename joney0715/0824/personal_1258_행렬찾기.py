import sys

sys.stdin = open('input_1258.txt', 'r')

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    n = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    i = j = 0
    matrix_list = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] and not visit[i][j]:
                row = 0
                for y in range(i, n):   
                    if not matrix[y][j]:
                        break
                    row += 1
                    col = 0
                    for x in range(j, n):   
                        if not matrix[y][x]:
                            break
                        col += 1
                        visit[y][x] = True
                matrix_list.append([row,col])      
        
    cnt = 0
    for _ in matrix_list:
        cnt += 1
    for p in range(cnt):
        for q in range(p, cnt):
            if matrix_list[p][0] * matrix_list[p][1] >= matrix_list[q][0] * matrix_list[q][1]:
                matrix_list[p], matrix_list[q] = matrix_list[q], matrix_list[p]
    print('#{}'.format(tc), cnt, end=' ')
    for m in matrix_list:
        print(*m, end=' ')
    print()