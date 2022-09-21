
N = int(input())

# 도우 가격, 토핑 가격
A, B = map(int, input().split())

# 도우 열량
C = int(input())

# 토핑 열량
D_list = []
for _ in range(N):
    D = int(input())
    D_list.append(D)

# 토핑 열량을 내림차순으로 정렬
D_list = sorted(D_list, reverse=True)

# 토핑이 없는 경우를 초기값으로 설정
max_value = C // A

# 열량이 높은 것부터 하나씩 추가하면서 1원당 열량 계산
for i in range(N):
    value = (C + sum(D_list[:i+1])) // (A + ((i+1) * B))

    # 최대값 비교
    if value > max_value:
        max_value = value
print(max_value)