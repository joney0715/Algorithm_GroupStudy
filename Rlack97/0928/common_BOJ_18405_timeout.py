# 18405_경쟁적 전염  풀이
# 2022-09-25
import copy

N, K = map(int,input().split())

pipes = [list(map(int,input().split())) for _ in range(N)]

S,X,Y = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def VIRUS(nothing):
    global prev_board

    for k in range(1,K+1):
        # 각 바이러스 만큼 진행, 작은 수부터.

        for i in range(N):
            for j in range(N):
            # 이전 상태를 기록해놓은 리스트를 순회하면서

                if prev_board[i][j] == k:
                    # 동일 숫자의 바이러스가 확인되었을 때 작업 진행


                    for a in range(4):
                        nx = i+dx[a]
                        ny = j+dy[a]
                        # 4방향 순회

                        if 0 <= nx < N and 0<= ny <N and prev_board[nx][ny] == 0: 
                            pipes[nx][ny] = k
                            # 인덱스 검증 및 비어있는 칸인지 확인 후 전염

    

for i in range(S):
    prev_board = copy.deepcopy(pipes) # 완전복제
    VIRUS(0)
    

print(pipes[X-1][Y-1])

# 시간초과 엔딩..