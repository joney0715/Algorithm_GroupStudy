import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    aplicants = [0]*(N+1)
    for _ in range(N):
        first, second = map(int,input().split())
        aplicants[first] = second 
        # 한 쪽 성적을 기준으로 정렬

    answer = 1
    # 1등한 사람은 어쨌든 통과하므로
    top = aplicants[1]
    # 읽어들이는 순서에서 가장 등수가 낮은 합격자

    for i in range(2,N+1):
        if top > aplicants[i]:
            # 가장 등수가 낮은 합격자보다 등수가 높은가?
            # 배열 순서상 이미 한 쪽의 성적에서 지고 있으므로,
            # 이쪽에서도 등수가 더 낮으면 합격할 수 없음
            answer += 1

            # 조건을 통과했다면 합격 가능인수를 증가

            top = aplicants[i]
            # 가장 등수가 낮은 합격자 갱신

                
    print(answer)


# readline으로 시간단축해서 통과.... 진짜 돌겠네