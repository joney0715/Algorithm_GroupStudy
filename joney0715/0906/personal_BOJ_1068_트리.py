
def dfs(node):
    global cnt

    # 이미 한번 방문한 곳에 간 경우
    if visit[node]:
        return

    # 제거된 노드에 도착한 경우
    if node == d:
        return

    # 리프 노드에 도착한 경우
    if not len(tree[node]):
        cnt += 1

    visit[node] = True
    for n in tree[node]:
        dfs(n)

N = int(input())

N_list = list(map(int, input().split()))
d = int(input())

delete = [d]
tree = [[] for _ in range(N)]
for i in range(N):
    # 루트 노드인 경우
    if N_list[i] == -1 or i == d:
        continue

    # 제거된 노드와 연결된 경우
    # 트리에 넣지 않음
    if N_list[i] in delete:
        delete.append(i)
        continue

    # 그 외
    tree[N_list[i]].append(i)

print(tree)

visit = [False] * N
cnt = 0
for n in range(N):
    if N_list[n] == -1:
        dfs(n)

print(cnt)