# 이거 왜 안됨??
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

n = 3
course = [[0,1], [0,2], [1,2]]

graph = [[] for _ in range(n)]
for x in course:
    graph[x[0]].append(x[1])

visit = [False] * 100

for x in range(n):
    if not dfs(x):
        answer =  False
        break
else:
    answer = True

print(answer)