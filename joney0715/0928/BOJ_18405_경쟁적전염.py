from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(position):
    queue = deque(position)

    while queue:
        virus, x, y, time = queue.popleft()

        if time == S:
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not plate[nx][ny]:
                plate[nx][ny] = virus
                queue.append((virus, nx, ny, time+1))

N, K = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X -= 1
Y -= 1

position = []
for x in range(N):
    for y in range(N):
        if plate[x][y]:
            position.append((plate[x][y], x, y, 0))
position.sort()

bfs(position)

print(plate[X][Y])