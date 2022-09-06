import collections


def dfs(i):
    if i in trace:
        return False

    if i in visit:
        return True

    trace.append(i)
    for y in graph[i]:
        if not dfs(y):
            return False
    trace.remove(i)

    visit.append(i)

    return True

course = [[0,1], [0,2], [1,2]]

graph = collections.defaultdict(list)
for x,y in course:
    graph[x].append(y)

visit = []
trace = []

for x in list(graph):
    if not dfs(x):
        answer = False
        break
else:
    answer = True

print(answer)
