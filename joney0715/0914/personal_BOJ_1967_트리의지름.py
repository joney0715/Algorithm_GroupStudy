from collections import defaultdict, deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visit[node] = 0

    while queue:
        n = queue.popleft()

        for i, d in tree[n]:
            if visit[i] == -1:
                queue.append(i)
                visit[i] = visit[n] + d

N = int(input())

tree = defaultdict(list)
for _ in range(N-1):
    s, e, d = map(int, input().split())
    tree[s].append((e,d))
    tree[e].append((s,d))

visit = [-1] * (N+1)
visit[1] = 0
bfs(1)

end_node = visit.index(max(visit))
visit = [-1] * (N+1)
visit[end_node] = 0
bfs(end_node)

print(max(visit))