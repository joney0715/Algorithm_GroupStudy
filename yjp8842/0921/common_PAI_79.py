# 내 풀이

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

sort_people = sorted(people, key = lambda x : (-x[0], x[1]))
# [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]

re_sort = []
for i in range(len(sort_people)):
    p = sort_people.pop(0)
    re_sort.insert(p[1], p)
    
print(re_sort)


# 교재 풀이

import heapq

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

heap = []
# 키가 최대인 사람 먼저 추출할 수 있도록 최대 힙 구성
for p in people:
    heapq.heappush(heap, (-p[0], p[1]))

# 키가 최대인 사람 먼저 추출
result = []
while heap:
    p = heapq.heappop(heap)
    result.insert(p[1], [-p[0], p[1]])

print(result)

# [[7, 0]] : 0번째 인덱스에 [7, 0] 삽입
# [[7, 0], [7, 1]] : 1번째 인덱스에 [7, 1] 삽입
# [[7, 0], [6, 1], [7, 1]] : 1번째 인덱스에 [6, 1] 삽입
# [[5, 0], [7, 0], [6, 1], [7, 1]] : 0번째 인덱스에 [5, 0] 삽입
# [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]] : 2번째 인덱스에 [5, 2] 삽입
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]] : 4번째 인덱스에 [4, 4] 삽입