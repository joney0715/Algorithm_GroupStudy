from collections import deque

def bfs(node):
    global answer
    queue = deque()
    queue.append(node)
    visit[node] = 1

    while queue:
        n = queue.popleft()

        if visit[n] <= 3:
            answer += 1 

        for i in graph[n]:
            if not visit[i]:
                queue.append(i)
                visit[i] = visit[n] + 1
                

N = int(input())

E = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (N+1)
answer = 0
if not len(graph[1]):
    print(0)
else:
    bfs(1)
    print(answer-1)
