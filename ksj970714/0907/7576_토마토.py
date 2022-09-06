from collections import deque
import sys

M,N = map(int,input().split())
tomato = []

for i in range(N):
    tomato.append(list(map(int,sys.stdin.readline().split())))


dq = deque()
delta = [[1,0],[-1,0],[0,1],[0,-1]] #델타탐색 + BFS
count = -1 #일단 모든 토마토가 익은 시점에도 루프가 한번 돌기 때문에, 카운트는 -1부터 시작.
rawtomato = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            dq.append([i,j])
        elif tomato[i][j] == 0:
            rawtomato += 1


    #스택에 집어넣고, 연산을 모두 한 뒤 빼주는 아이디어
    #스택에 더 이상 들어갈것이 없으면 끝
while dq:
    for idx in range(len(dq)):
        curtomato = dq.popleft()
        for _ in range(4):
            a = delta[_][0] + curtomato[0]
            b = delta[_][1] + curtomato[1]
            if 0<=a<=N-1 and 0<=b<=M-1:
                if tomato[a][b]==0:
                    dq.append([a,b])
                    tomato[a][b]=1
                    rawtomato -= 1
    count += 1

if rawtomato == 0 :
    print(count)
else:
    print(-1)


