# 17141_연구소2 풀이
# 2022-09-26

from collections import deque
from itertools import combinations

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 4방향 탐색

def BFS(v):
    queue = deque(v)
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    m = 0
    # -1 값으로 방문리스트 생성, 덱 생성

    for x,y in queue:
        visited[x][y] = 0
        # 바이러스를 둔 구간을 0으로 변경
    
    while queue:
        x,y = queue.popleft()
        # 들어온 순서데로 popleft

        for i in range(4):
            hx = x+dx[i]
            hy = y+dy[i]

            if 0 <= hx < N and 0 <= hy < N and visited[hx][hy] == -1 and lab[hx][hy] != 1:
                # 4방향 탐색 + 방문 한 적 없음 + 벽이 아님
                queue.append([hx,hy])
                # 큐에 다음 지점을 저장
                visited[hx][hy] = visited[x][y] + 1
                # 전파 시간 기록
                m = max(m,visited[hx][hy])
                # 몇 초가 걸리는지 비교해서 저장
    
    # 감염 못시키는 칸 검사
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and lab[i][j] != 1:
                return float('inf')
                # float inf를 박아버려서 값을 구분
    
    return m



N, M = map(int,input().split())

lab = [list(map(int,input().split())) for _ in range (N)]


V = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            V.append((i,j))
            lab[i][j] = 0


answer = float('inf')

for v in combinations(V,M):
    answer = min(BFS(v), answer)
    # 각 조합마다 BFS를 실행

if answer == float('inf'):
    print(-1)
else:
    print(answer)

