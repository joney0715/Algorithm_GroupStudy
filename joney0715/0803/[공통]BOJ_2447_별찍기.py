
def star(x, y, N):
<<<<<<< HEAD
=======
    # 3개인 경우 점 찍기
>>>>>>> 968b9676e538e2a29a038070dacbb42d8f898308
    if N == 3:
        M[x][y] = M[x][y+1] = M[x][y+2] = '*'
        M[x+1][y] = M[x+1][y+2] = '*'
        M[x+2][y] = M[x+2][y+1] = M[x+2][y+2] = '*'
    else:
<<<<<<< HEAD
        n = N // 3
=======
        # 일정한 패턴이 3개씩 나오기 때문에 3으로 나눔
        n = N // 3
        # 첫번째 줄
>>>>>>> 968b9676e538e2a29a038070dacbb42d8f898308
        star(x, y, n)
        star(x+n, y, n)
        star(x+(2*n), y, n)

<<<<<<< HEAD
        star(x, y+n, n)       
        star(x+(2*n), y+n, n)

=======
        # 두번째 줄
        star(x, y+n, n)       
        star(x+(2*n), y+n, n)

        # 세번째 줄
>>>>>>> 968b9676e538e2a29a038070dacbb42d8f898308
        star(x, y+(2*n), n)
        star(x+n, y+(2*n), n)
        star(x+(2*n), y+(2*n), n)

<<<<<<< HEAD
#N = int(input())
N = 9
M = [[' '] * N for _ in range(N)]

star(0, 0, N)
for i in M:
    print(''.join(i))

# def print_star(x, y, n):
#     if n == 3:
#         ans[x][y] = '*'
#         ans[x+1][y-1] = ans[x+1][y+1] = '*'
#         for i in range(-2, 3):
#             ans[x+2][y+i] = '*'
#     else:
#         nn = n // 2
#         print_star(x, y, nn)
#         print_star(x+nn, y-nn, nn)
#         print_star(x+nn, y+nn, nn)
=======
N = int(input())
# 점을 찍기위한 맵 생성
M = [[' '] * N for _ in range(N)]

# 함수 불러오기
star(0, 0, N)

# 점 찍기
for i in M:
    print(''.join(i))

>>>>>>> 968b9676e538e2a29a038070dacbb42d8f898308
