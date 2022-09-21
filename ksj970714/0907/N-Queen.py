global N
N = int(input())
visited = [0]*N #체스판의 가로 체크
arr = []
for i in range(N+1):
    arr.append(visited[:])

leftright = {} #좌측 상단에서 우측 아래로, c와 r의 차가 같은 대각선.
for i in range(1-N,N):
    leftright[i] = 0
rightleft = {} #우측에서 좌측으로, 즉, r과 c의 합이 같은 대각선
for i in range(2*N-1):
    rightleft[i] = 0

def queen(depth):
    global able
    if depth == N:
        able += 1
        return
    for i in range(N):
        if visited[i] == 0 and leftright[depth-i] == 0 and rightleft[depth+i] == 0:
            visited[i] = 1
            leftright[depth - i] = 1
            rightleft[depth + i] = 1
            queen(depth + 1)

            visited[i] = 0
            leftright[depth - i] = 0
            rightleft[depth + i] = 0


able = 0
queen(0)
print(able)