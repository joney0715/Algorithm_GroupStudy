import collections

def dfs(i):
    if visit[i]:
        return False
    
    visit[i] = True
    for y in graph[i]:
        if not dfs(y):
            return False
    visit[i] = False

    return True

course = [[0,1], [0,2], [1,2]]

graph = collections.defaultdict(list)
for x,y in course:
    graph[x].append(y)

visit = [False] * 100

for x in list(graph):
    if not dfs(x):
        answer =  False
        break
else:
    answer = True

print(answer)