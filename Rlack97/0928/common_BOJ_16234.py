# 16234_인구이동  풀이
# 2022-09-24

import sys
sys.setrecursionlimit(10000)
# 재귀 제한 수 증가

N, L, R = map(int,input().split())
populations = [list(map(int,input().split())) for _ in range(N)]
day = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]
# 상하좌우 좌표

def DFS(i,j):

    visited[i][j] = 1
    location.append((i,j))
    # 방문처리 및 해당 위치 인덱스 기록

    for a in range(4):
        # 4방향 탐색
        nx = i+dx[a]
        ny = j+dy[a]
        # 계산 반복을 줄이기 위한 변수 지정

        if 0 <= nx < N and 0 <= ny < N and L <= abs(populations[i][j] - populations[nx][ny]) <= R and not visited[nx][ny]:
            # 인덱스 값이 valid하고, 방문한 적이 없으며, 차이값이 조건에 맞는 경우
    
            DFS(nx,ny)
            #해당 국가로 재귀

# DFS 함수

while True:
    visited = [[0]*N for _ in range(N)]     
    flag = False

    for i in range(N):
        for j in range(N):
            location = []

            if visited[i][j] == 0:
                DFS(i,j)
                
            if len(location) > 1:
                flag = True
                lo_sum = 0
                for x,y in location:
                    lo_sum += populations[x][y]
                    # 2개 이상일 때만 값을 구해야 계산 수를 줄일 수 있음

                after_day = lo_sum // len(location)
                
                for a,b in location:
                    populations[a][b] = after_day

    if not flag:
        print(day)
        break

    day += 1