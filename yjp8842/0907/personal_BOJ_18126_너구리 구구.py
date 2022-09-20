# 예시출력1만 고려한 답안
""" N = int(input())
arr = []
for _ in range(N - 1):
    arr.append(list(map(int, input().split())))

rooms = [[] for _ in range(N + 1)]
road_len = [[] for _ in range(N + 1)]
for i in range(len(arr)):
    rooms[arr[i][0]].append(arr[i][1])
    road_len[arr[i][1]].append(arr[i][2])

cnt = 0    
for i in rooms[1]:
    cnt += road_len[i][0]
    if rooms[i]:
        j = max(rooms[i])
        cnt += road_len[j][0]
        
print(cnt) """



# 풀이 참고 답안

N = int(input())
rooms = [[] for _ in range(N + 1)]

# 각 노드에서 갈 수 있는 노드를 모두 저장
for i in range(N - 1):
    A, B, C = map(int, input().split())
    rooms[A].append([B, C])
    rooms[B].append([A, C])

visited = [0] * (N + 1)

stack = [[1, 0]]

result = 0
while stack:
    v, l = stack.pop()
    visited[v] = 1
	
    # leaf node : 자식이 없는 노드
    # leaf node 인지 판별
    flag = False
    # 현재 v 노드가 갈 수 있는 곳이 한곳이라도 있다면 leaf 노드가 아님
    for tmpv, tmpl in rooms[v]:
        if visited[tmpv] == 0:
            flag = True
	
    # leaf node가 아닌 경우, 스택에 저장
    # 자식 노드가 있는 경우
    if flag == True:
        if rooms[v]:
            for nv, nl in rooms[v]:
                if visited[nv] == 0:
                    stack.append([nv, l + nl])
                    
    # leaf node인 경우, 최대값 갱신
    else:
        if l > result:
            result = l

print(result)