from collections import deque

# DFS 함수
def dfs(node):
    # 노드 방문 처리
    visit[node] = True

    # 방문한 노드 출력
    print(node, end=' ')

    # 작은 노드부터 처리하기 위해서 정렬
    graph[node].sort()

    # 연결된 노드 하나씩
    for n in graph[node]:
        # 미방문인 경우 해당 노드에 대해 재귀
        if not visit[n]:
            dfs(n)
    return True

# BFS 함수
def bfs(node):
    # 큐로 사용할 덱 정의
    # 해당 노드 덱에 삽입
    que = deque([node])
    # 해당 노드 방문 처리
    visit[node] = True

    # 큐에 요소가 없어질 때까지 반복
    while que:
        # 큐에서 요소 제거
        n = que.popleft()
        # 제거된 요소는 처리가 끝났으므로 출력
        print(n, end=' ')

        # 작은 노드부터 처리하기 위해 정렬
        graph[n].sort()

        # 연결된 노드 하나씩
        for i in graph[n]:
            # 미방문인 경우
            if not visit[i]:
                # 큐에 추가후 방문 처리
                que.append(i)
                visit[i] = True

N, M, V = map(int, input().split())

# 그래프 구조 만들기
# 인접 리스트 사용
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visit = [False] * (N+1)
dfs(V)
print()
visit = [False] * (N+1)
bfs(V)