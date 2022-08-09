import heapq
import sys

# 연산 개수
N = int(sys.stdin.readline())

# 힙 초기화
heap = []
for _ in range(N):
    # 숫자 입력
    n = int(sys.stdin.readline())
    
    # n이 0인 경우 가장 작은 값 출력
    # 값이 없는 경우 0 출력
    if n == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    
    # n이 0이 아니면 힙에 추가
    else:
        heapq.heappush(heap, n)
