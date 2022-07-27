
def star(x, y, N):
    if N == 3:
        M[x][y] = M[x][y+1] = M[x][y+2] = '*'
        M[x+1][y] = M[x+1][y+2] = '*'
        M[x+2][y] = M[x+2][y+1] = M[x+2][y+2] = '*'
    else:
        n = N // 3
        star(x, y, n)
        star(x+n, y, n)
        star(x+(2*n), y, n)

        star(x, y+n, n)       
        star(x+(2*n), y+n, n)

        star(x, y+(2*n), n)
        star(x+n, y+(2*n), n)
        star(x+(2*n), y+(2*n), n)

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
