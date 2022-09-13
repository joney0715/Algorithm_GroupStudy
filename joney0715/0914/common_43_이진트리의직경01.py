# 내 풀이

from collections import defaultdict, deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visit[node] = 0

    while queue:
        n = queue.popleft()

        for i in tree[n]:
            if visit[i] == -1:
                queue.append(i)
                visit[i] = visit[n] + 1

# 입력값
nums = [1,2,3,4,5]

# 트리 구조 만들기
# 이 방법의 오류 이진트리의 가지가 하나인 경우 오류 남
tree = defaultdict(list)
for n in range(len(nums)):
    if 2*n+1 < len(nums) and nums[2*n+1] != 'NULL' and 2*n+2 < len(nums) and nums[2*n+2] != 'NULL':        
        tree[nums[n]].append(nums[2*n+1])
        tree[nums[n]].append(nums[2*n+2])
        tree[nums[2*n+1]].append(nums[n])
        tree[nums[2*n+2]].append(nums[n])


visit = [-1] * 100
visit[1] = 0
bfs(1)

end_node = visit.index(max(visit))
visit = [-1] * 100
visit[end_node] = 0
bfs(end_node)

print(max(visit))