import sys

# 계속 시간 초과나서 sys 사용
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    N_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # 서류 심사 결과로 정렬
    N_list.sort()
    
    # 서류 심사 1등은 자연스럽게 채용
    count = 1

    # 이후 면접 심사 결과로 비교
    k = N_list[0][1]

    # 나머지에 대해 반복
    for i in range(1,N):
        # 서류 1등보다 면접 등수가 낮으면 불합격
        # 면접 결과가 더 좋은 사람들만
        if N_list[i][1] < k:
            count += 1

            # 비교할 면접 결과 초기화
            k = N_list[i][1]

    print(count)