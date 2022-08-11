import sys
import heapq                      # 우선순위 큐를 위한 임포트
input = sys.stdin.readline

t = int(input())

for _ in range(t):               # 테스트 케이스 수만큼 반복
    minHeap = []
    maxHeap = []                 # 최솟값 heap과 최댓값 heap을 초기화
    k = int(input())
    visited = [False] * k          # visited 리스트 생성
    
    for i in range(k):            # 입력 데이터의 수만큼 반복
        Word, num = input().split()     # 입력값을 변수에 저장 

        if Word == "I":          # 앞부분이 I일 경우, 정수 num을 Q에 삽입한다.
            heapq.heappush(minHeap,(int(num),i))            # 최댓값. 최솟값 힙에 전부 삽입하면서 삽입 순서도 튜플로 같이 기록
            heapq.heappush(maxHeap,(-int(num),i))           # 최댓값의 경우 -를 붙여준 후, 출력할 때 다시 -를 사용한다.
            visited[i] = True      # 해당 순서의 visited 리스트를 True로 변경              

        else:     # 앞부분이 D일 경우, 1이면 최댓값을, -1이면 최솟값을 삭제한다
            if num == '-1':
                while minHeap and not visited[minHeap[0][1]]:          
                    heapq.heappop(minHeap)
                    #최소치의 삽입 순서를 인덱스로 하는 visited 리스트의 요소가 False일 때, 즉 해당 방문 값이 삭제되었을 때
                    #최솟값을 제거
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)
                    # 만약 방문값이 True 상태라면, visited 리스트 값을 False로 바꾸고
                    # 최솟값을 제거
            else:
                while maxHeap and not visited[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
                    # 최댓값의 경우에도 똑같이 동작한다.

    while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and not visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
        # 최댓값 큐 혹은 최솟값 큐 어느 한 쪽에서라도 그 값이 제거되었으면, 반대쪽 큐에서도 제거한다.

    if not minHeap or not maxHeap:
        print("EMPTY")
        # 이때, 어느 쪽이던 큐가 비어있다면 empty 출력
    else:
        a = maxHeap[0][0] * (-1)
        b = minHeap[0][0]
        print(a,b)
        #구한 최댓값, 최솟값을 출력한다