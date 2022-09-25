# 18405_경쟁적 전염  풀이
# 2022-09-25

import sys
sys.setrecursionlimit(10000)

N, K = map(int,input().split())

pipes = [list(map(int,input().split())) for _ in range(N)]

S,X,Y = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(plist,loca,time,obj):
    if time == obj:
        return plist
    # 규정 시간에 도달하면 리스트 반환

    nxtloca = []
    for i in loca:
        for a in range(4):
            nx = i[0]+dx[a]
            ny = i[1]+dy[a]
            # 4방향 순회

            if 0 <= nx < N and 0<= ny <N and plist[nx][ny] == 0: 
                plist[nx][ny] = i[2]
                nxtloca.append((nx,ny,i[2]))
                # 인덱스 검증 및 비어있는 칸인지 확인 후 전염

    
    return BFS(plist,nxtloca,time+1,obj)
    # 반환되어 온 리스트를 계속 반환

    
location = []
for i in range(N):
    for j in range(N):
        if pipes[i][j] != 0:
            location.append((i,j,pipes[i][j]))
            # 바이러스들의 위치정보 리스트
location.sort(key=lambda x : x[2])
# 바이러스 크기대로 정렬

answer = BFS(pipes,location,0,S)

print(answer[X-1][Y-1])

