import heapq

N = int(input())

# 정수 행렬의 첫 번째 행을 입력
heap = list(map(int, input().split()))
# 힙 구조화
heapq.heapify(heap)

# 두 번째 행부터 입력
for _ in range(1,N):
    row = list(map(int, input().split()))
    
    # 입력 받은 리스트를 정렬
    row.sort()

    # 입력 받은 리스트의 가장 작은 값부터 처리
    # 이 반복문으로 N개의 요소를 가진 힙은
    # 가장 큰 N개의 값이 들어있는 힙으로 갱신됨
    for j in row:
        # 첫번째 행의 가장 작은 값보다 
        # 입력 받은 리스트의 가장 작은 값이 크다면
        # 힙에 넣고 기존에 힙에 있던 값은 추출
        if j > heap[0]:
            heapq.heappush(heap, j)
            heapq.heappop(heap)

# 연산이 끝난 힙은 N개의 가장 큰 수가 들어있기 때문에
# 가장 작은 값을 빼면 N번째로 큰 수가 나옴
print(heap[0])

'''
숫자를 하나씩 비교하거나 전체 숫자를 힙을 써서 처리하면 메모리가 부족함
메모리 부족을 막기위해 최소한의 요소를 가진 리스트만 써야함
'''

