from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 조합을 찾는 함수
def combinate(n, c):
    if len(c) == M:
        combination.append(c)
    
    for i in range(n, len(available)):
        if available[i] not in c:
            combinate(i+1, c+[available[i]])


# 바이러스 전파
def bfs(virus):
    queue = deque(virus)
    result = 0
    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not lab[nr][nc] and visit[nr][nc]==-1:
                visit[nr][nc] = visit[r][c] + 1
                result = max(visit[nr][nc], result)
                queue.append((nr, nc))
    
    # 전염 안 된 곳 찾기
    for row in range(N):
        for col in range(N):
            if lab[row][col] == 0 and visit[row][col] == -1:
                result = 1000000

    return result


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 바이러스를 놓을 수 있는 곳 탐색
available = []
for r in range(N):
    for c in range(N):
        if lab[r][c] == 2:
            available.append((r,c))
            lab[r][c] = 0

# 조합
combination = []
combinate(0, [])

# 각 조합에 대해서 전파 시간 계산
answer = []
for combi in combination:
    visit = [[-1]*N for _ in range(N)]
    for r,c in combi:
        visit[r][c] = 0
    result = bfs(combi)
    answer.append(result)

# 전파 시간이 가장 짧은 조합
ans = min(answer)
if ans == 1000000:
    print(-1)
else:
    print(ans)