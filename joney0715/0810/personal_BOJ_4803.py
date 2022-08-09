import sys

# 트리인지 아닌지 판별하는 함수
# 재귀를 사용하여 미방문 노드를 탐색
def find_tree(pre_node, node): # 전 노드, 해당 노드

    # 해당 노드 방문 처리
    visit[node] = True

    # 해당 노드에 연결되어 있는 노드들 하나씩 처리
    for k in tree[node]:
        # 연결되어 있는 노드가 직전에 처리한 노드라면 넘어감
        if pre_node == k:
            continue

        # 연결되어 있는 노드가 이미 방문 상태라면 사이클
        if visit[k]:
            return False

        # 연결되어 있는 노드를 다시 함수에 넣기 (재귀)
        result = find_tree(node, k)
        # 재귀의 결과가 False라면 사이클이라는 증거
        if not result:
            return False
    # 연결되어 있는 노드가 전부 미방문이었다면 트리
    return True

testcase = 0
while True:
    testcase += 1
    # 노드 수, 간선 수 입력
    N, M = sys.stdin.readline().split()
    N, M = int(N), int(M)

    # 입력이 0 0 이라면 중단
    if N == 0 and M == 0:
        break

    # 방문 처리를 위한 리스트
    visit =[False] * (N+1)

    # 그래프 구조 만들기 위한 리스트 
    # 인접 리스트 방식 선택
    tree = [[] for _ in range(N+1)]

    # 간선 정보를 하나씩 받아서 완성
    for i in range(M):
        start, end = sys.stdin.readline().split()
        start, end = int(start), int(end)
        # 양방향 간선으로 하지 않으면 반례가 있음 (아래 참조)
        tree[start].append(end)
        tree[end].append(start)

    # 노드 하나씩 함수에 넣어서 트리인지 아닌지 확인
    # 트리라면 하나씩 카운트
    count = 0
    for j in range(1, N+1):
        if not visit[j]:
            if find_tree(0, j):
                count += 1                

    if count == 0:
        print(f'Case {testcase}: No trees.')
    elif count == 1:
        print(f'Case {testcase}: There is one tree.')
    else:
        print(f'Case {testcase}: A forest of {count} trees.')

# 단방향 트리로 했을 경우 틀림
# 반례
# 노드6 간선5
# 1 2
# 2 3
# 3 4
# 5 2
# 6 1
# 의 경우 사이클이 없는데도 트리가 아닌 경우가 되어버림
