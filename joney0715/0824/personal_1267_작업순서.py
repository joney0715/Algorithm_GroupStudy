
# 해당 노드(작업)을 하기 전에 해야하는
# 작업이 뭐가 있는지 찾는 함수
def linked_process(node):
    pre = []
    for i in range(1, V+1):
        # 모든 노드에 대해서 입력된 노드가 연결된 노드 찾기
        if node in graph[i]:
            pre.append(i)
    return pre

# 해당 작업을 하기위해 실행해야하는 작업이
# 실행됐는지 확인하는 함수
def done_process(node):
    # 전 작업 탐색
    pre = linked_process(node)

    # 전 작업이 하나라도 실시되지 않은 경우
    for i in pre:
        if node in graph[i] and not visit[i]:
            return False

    # 전부 실시된 경우
    return True   

# dfs를 사용한 작업 실행
def process(node):
    # 작업 완료 처리
    visit[node] = True
    # 작업 리스트에 저장
    answer.append(node)

    # 다음 연결된 작업
    for n in graph[node]:
        # 해당 작업이 미실행이면서 전 작업들이 모두 실행된 경우
        if not visit[n] and done_process(n):
            process(n)

T = 10
for tc in range(1, T+1):
    # 노드와 간선 수
    V, E = map(int, input().split())

    # 간선 정보
    E_list = list(map(int, input().split()))

    # 그래프
    graph = [[] for _ in range(V+1)]
    
    # 간선 정보를 풀어서 그래프에 표시
    i = j = 0
    while i < E:
        # 단일 방향
        graph[E_list[j]].append(E_list[j+1])
        j += 2
        i += 1

    # 방문 리스트
    visit = [False] * (V+1)

    # 작업 순서를 저장할 리스트
    answer = []

    # 노드를 하나씩 작업할 순서인지 확인
    for node in range(1, V+1):
        # 첫 작업인 경우만 처리
        # linked_process의 반환값이 비어있으면
        # 해당 작업을 하기 전에 해야하는 작업이 없다는 뜻
        if not linked_process(node):
            process(node)
    print('#{}'.format(tc), *answer)