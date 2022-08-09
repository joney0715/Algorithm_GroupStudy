import heapq
import sys

# 다른 힙에서 제거된적이 있는 요소를 제거하기 위한 함수
# 힙과 방문 처리 리스트가 파라미터
def delete(que, v):
    # 힙이 비어있지 않고, 미방문인 경우 반복
    # visit[i]가 False라면 다른 힙에서 제거된 요소라는 것
    # 반복문으로 타겟의 수(방문이 True)가 나올때까지 전부 제거 
    while que and not v[que[0][1]]:
        heapq.heappop(que)

#테스트 케이스 수
T = int(input())

for _ in range(T):
    # 입력 개수
    N = int(input())
    # 최소힙, 최대힙 하나씩 정의
    que_min = []
    que_max = []
    # 방문 처리를 위한 리스트 정의
    visit = [False] * N

    for i in range(N):
        # 상태(I or D)와 숫자 입력
        s, n = sys.stdin.readline().split()

        # I 라면 최소힙과 최대힙 양쪽에 숫자 삽입       
        if s == 'I':
            # 삽입을 할때 삽입된 요소의 인덱스를 같이 넣어둠
            heapq.heappush(que_min, (int(n), i))
            heapq.heappush(que_max, (-int(n), i))
            visit[i] = True # 방문 처리

        # D 인 경우
        else:
            # 1인경우 최대힙에서 요소 하나 제거
            if n == '1':
                # 다른 힙에서 제거된 요소 제거
                delete(que_max, visit)
                if que_max:
                    # 방문을 False로 하고 제거
                    visit[que_max[0][1]] = False
                    heapq.heappop(que_max)

            # -1인 경우 최소힙에서 요소하나 제거
            else:
                # 다른 힙에서 제거된 요소 제거
                delete(que_min, visit)
                if que_min:
                    # 방문을 False로 하고 제거
                    visit[que_min[0][1]] = False
                    heapq.heappop(que_min)

    # 마지막으로 쓸모없는 요소 전부 제거                
    delete(que_max, visit)
    delete(que_min, visit) 

    if not que_min or not que_max:
        print("EMPTY")
    else:
        print(-que_max[0][0], que_min[0][0])