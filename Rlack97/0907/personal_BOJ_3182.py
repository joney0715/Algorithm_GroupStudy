# 한동이는 공부가 하기 싫어 풀이
# 2022-09-01

N = int(input())
senpai = [0]*(N+1)

for n in range(1,N+1):
    dialogue = int(input())
    senpai[n] = dialogue
# 입력값 받음
# 모든 그래프의 노드가 방향성 간선 하나만을 가지므로 stack사용 불필요,
# visited 리스트를 통해 한 순환이 끝나는 시점에서 카운트를 멈추면 된다

def DFS(graph,start):
    visited = [0]*(N+1)
    # 방문리스트

    visited[start] = True
    
    # 첫 값을 방문처리 
    a = start
    cnt = 1
    # 기본 카운트, 값 변경을 위한 변수지정
    
    while True:
        if visited[graph[a]] == 0:
            # 목적지에 방문한 적이 없다면
            a = graph[a]
            # 위치를 이동하고
            visited[a] = True
            # 방문처리를 하고
            cnt += 1
            # 카운트
        else:
            break
    return cnt


answer = 0
num = 0
for i in range(1,N+1):
    k =  DFS(senpai,i)
    # 시작지점이 다를 때의 카운트 수들
    if answer < k:
        answer = k
        num = i
        # 카운트를 비교해서, 클 때만 (같아도 갱신하면 가장 큰 수의 num이 나오므로) 갱신

print(num)
# num을 출력