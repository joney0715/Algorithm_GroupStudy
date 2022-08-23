
def linked_process(node):
    pre = []
    for i in range(1, V+1):
        if node in graph[i]:
            pre.append(i)
    return pre

def done_process(node):
    pre = linked_process(node)
    for i in pre:
        if node in graph[i] and not visit[i]:
            return False
    return True   

def process(node):
    visit[node] = True
    answer.append(node)
    for n in graph[node]:
        if not visit[n] and done_process(n):
            process(n)

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))

    graph = [[] for _ in range(V+1)]
    i = j = 0
    while i < E:
        graph[E_list[j]].append(E_list[j+1])
        j += 2
        i += 1
    visit = [False] * (V+1)
    answer = []
    for node in range(1, V+1):
        if not linked_process(node):
            process(node)
    print('#{}'.format(tc), *answer)