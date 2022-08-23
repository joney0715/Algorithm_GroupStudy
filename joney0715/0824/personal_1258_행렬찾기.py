import sys

sys.stdin = open('input_1258.txt', 'r')

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    n = int(sys.stdin.readline())

    # 행렬 입력
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # 방문 리스트
    visit = [[False] * n for _ in range(n)]

    matrix_list = []
    for i in range(n):
        for j in range(n):
            # 요소가 0이 아니면서 방문한적이 없는 경우
            if matrix[i][j] and not visit[i][j]:
                row = 0
                # i,j로 시작하는 행렬 탐색
                # 행
                for y in range(i, n):
                    # 행의 첫 요소가 0인 경우 행의 크기가 결정됨
                    if not matrix[y][j]:
                        break
                    row += 1
                    col = 0
                    # 열
                    for x in range(j, n):   
                        # 값이 0인 행이 나오면 열의 크기가 결정됨
                        if not matrix[y][x]:
                            break
                        col += 1
                        visit[y][x] = True

                # 행렬의 행과 열의 개수를 리스트에 저장
                matrix_list.append([row,col])      
        
    # 행렬 개수 카운트
    cnt = 0
    for _ in matrix_list:
        cnt += 1
    
    # 행렬의 크기 순으로 정렬
    for p in range(cnt):
        for q in range(p, cnt):
            if matrix_list[p][0] * matrix_list[p][1] >= matrix_list[q][0] * matrix_list[q][1]:
                matrix_list[p], matrix_list[q] = matrix_list[q], matrix_list[p]
    
    # 결과 출력
    print('#{}'.format(tc), cnt, end=' ')
    for m in matrix_list:
        print(*m, end=' ')
    print()