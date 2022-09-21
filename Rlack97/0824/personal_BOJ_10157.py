X, Y = map(int,input().split())

seats = [[0]*X for _ in range(Y)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
# 디렉션 서치를 위한 리스트

K = int(input())
y, x, q = Y-1, 0, 0
seats[y][x] = 1
# 초기 위치 설정

for k in range(1, K):
    y += dy[q]
    x += dx[q]
    if y >= Y or x >= X or y < 0 or x < 0 or seats[y][x] != 0:
        y -= dy[q]
        x -= dx[q]
        # 범위를 벗어나거나 이미 방문한 곳일 경우 되돌아감

        q = (q + 1) % 4
        # 방향 변경

        y += dy[q]
        x += dx[q]

        if seats[y][x] != 0:
            print(0)
            quit()
            # 방향을 변경했는데도 갈 곳이 없다 = 해가 없음
    seats[y][x] = k+1
    # 횟수를 기록


print (x+1, Y-y)
