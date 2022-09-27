from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# dfs는 RecursionError
def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    visit[row][col] = True

    while queue:
        r, c = queue.popleft()
        changes.append((r, c))
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 내, 미방문인 나라
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                # 인구 차이 조건을 만족하는 경우
                if L <= abs(N_list[nr][nc] - N_list[r][c]) <= R:
                    visit[nr][nc] = True
                    queue.append((nr, nc))

N, L, R = map(int, input().split())
N_list = [list(map(int, input().split())) for _ in range(N)]


answer = 0
while True:
    flag = 0
    visit = [[False]*N for _ in range(N)]

    # 2차원 배열 탐색
    for r in range(N):
        for c in range(N):
            # 미방문시 해당 위치에서 bfs
            if not visit[r][c]:
                # 인구가 이동한 나라의 인덱스를 넣기 위한 리스트
                changes = []
                bfs(r, c)
                if len(changes) > 1:
                    flag = 1
                    
                    # 인구 이동
                    p = sum(N_list[r][c] for r,c in changes) // len(changes)
                    for c in changes:
                        N_list[c[0]][c[1]] = p

    if not flag:
        break

    answer += 1
        
print(answer)
