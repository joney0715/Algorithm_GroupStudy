# 내 풀이

from collections import defaultdict, deque


def bfs(node):
    queue = deque()
    queue.append(node)
    visit[node] = 1

    while queue:
        n = queue.popleft()
        
        for i in graph[n]:
            visit[i] = visit[n] + 1
            queue.append(i)

nums = [3, 9 ,20, 'NULL', 'NULL', 15, 7]

graph = defaultdict(list)
for n in range(len(nums)):
    if 2*n+1 < len(nums) and nums[2*n+1] != 'NULL':
        graph[nums[n]].append(nums[2*n+1])
    if 2*n+2 < len(nums) and nums[2*n+2] != 'NULL':
        graph[nums[n]].append(nums[2*n+2])

visit = [0] * 10000
bfs(list(graph)[0])
print(max(visit))