from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visit[1] = 1

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if not visit[i[0]]:
                queue.append(i[0])
                visit[i[0]] = visit[n] + i[1]

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e, d = map(int, input().split())

    graph[s].append((e, d))
    graph[e].append((s, d))

visit = [0] * (N+1)
bfs(1)

print(max(visit) - 1) 
