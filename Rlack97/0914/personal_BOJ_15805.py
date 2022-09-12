# 트리 나라 관광 가이드 풀이
# 2022-09-01

N = int(input())
input_list = list(map(int,input().split()))
K = max(input_list) + 1 
# 최대 숫자 + 0 갯수를 통해 K값을 알 수 있음

K_list = [0]*K
visited = [0]*K
# 연산에 필요한 공백 및 방문리스트 생성

for i in range(1,N):
    if visited[input_list[i]] == 0:
        # 방문한 적이 없는 곳에 가면
        K_list[input_list[i]] = input_list[i-1]
        # 직전에 방문한 곳이 해당 방문지의 부모 노드
        visited[input_list[i]] = 1
        # 방문처리

K_list[input_list[0]] = -1
# 시작점은 루트노드이므로 -1


print(K)
print(*K_list)