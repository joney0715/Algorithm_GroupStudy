from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = 0

    while queue:
        f = queue.popleft()

        # 이동 완료한 층수가 목표 층 수인 경우
        if f == G:
            return

        for i in (f+U, f-D):
            if 0 < i <= F and visit[i] == -1:
                visit[i] = visit[f] + 1
                queue.append(i)

# 건물 층 수, 현재 위치, 목표 위치, 위, 아래
F, S, G, U, D = map(int, input().split())

visit = [-1 for _ in range(F+1)]

# 현재 위치에서 bfs
bfs(S)

if visit[G]:
    print(visit[G])
else:
    print('use the stairs')