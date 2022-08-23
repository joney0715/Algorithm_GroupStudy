X, Y = map(int,input().split())

seats = [[0]*X for _ in range(Y)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

K = int(input())
y, x, q = Y-1, 0, 0
seats[y][x] = 1

for k in range(1, K):
    y += dy[q]
    x += dx[q]
    if y >= Y or x >= X or y < 0 or x < 0 or seats[y][x] != 0:
        y -= dy[q]
        x -= dx[q]

        q = (q + 1) % 4

        y += dy[q]
        x += dx[q]

        if seats[y][x] != 0:
            print(0)
            quit()
    seats[y][x] = k+1


print (x+1, Y-y)
