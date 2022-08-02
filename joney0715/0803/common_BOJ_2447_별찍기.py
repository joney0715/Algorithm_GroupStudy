
def star(x, y, N):
    # 3개인 경우 점 찍기
    if N == 3:
        M[x][y] = M[x][y+1] = M[x][y+2] = '*'
        M[x+1][y] = M[x+1][y+2] = '*'
        M[x+2][y] = M[x+2][y+1] = M[x+2][y+2] = '*'
    else:
        n = N // 3
        # 첫번째 줄
        star(x, y, n)
        star(x+n, y, n)
        star(x+(2*n), y, n)

        # 두번째 줄
        star(x, y+n, n)       
        star(x+(2*n), y+n, n)

        # 세번째 줄
        star(x, y+(2*n), n)
        star(x+n, y+(2*n), n)
        star(x+(2*n), y+(2*n), n)

N = int(input())
# 점을 찍기위한 맵 생성
M = [[' '] * N for _ in range(N)]

# 함수 불러오기
star(0, 0, N)

# 점 찍기
for i in M:
    print(''.join(i))

