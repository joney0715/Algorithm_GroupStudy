
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

D_list = sorted(D_list, reverse=True)

max_value = C // A
for i in range(N):
    value = (C + sum(D_list[:i+1])) // (A + ((i+1) * B))

    if value > max_value:
        max_value = value
print(max_value)