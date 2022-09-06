
def first(node, graph):
    if len(graph[node]) == 1: 
        return True
    else:
        return False

def second(node, graph):
    if len(graph[node]) == 2: 
        return True
    else:
        return False

def third(node, graph):
    if len(graph[node]) == 3: 
        return True
    else:
        return False

N = 12

graph = [[] for _ in range(N+1)]
for _ in range(N):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    if len(graph[i]) == 3:
        answer_list = [0, 0, 0]
        idx = i
        for n in graph[i]:
            if first(n, graph):
                answer_list[0] = 1
            if second(n, graph):
                answer_list[1] = 1
            if third(n, graph):
                answer_list[2] = 1

        if sum(answer_list) == 3:
            print(idx)
            break

