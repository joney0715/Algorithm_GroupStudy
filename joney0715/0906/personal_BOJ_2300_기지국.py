
N = int(input())

d = [0] * (N+1)

spot = []
for _ in range(N):
    x, y = map(int, input().split())
    spot.append((x, abs(y)))

# x축 기준으로 정렬
spot.sort()
# 0번째 인덱스 삽입
spot.insert(0, (0,0))

# 첫번째 건물부터
for i in range(1, N+1):
    # 초기값
    d[i] = 10000000

    # i번째 건물의 앞 건물의 y좌표로 초기화
    y = spot[i-1][1]

    # i번째 건물 앞 건물들
    for j in range(i-1, -1, -1):
        # i번째 건물의 y값과 비교하면서 y값을 최대값으로 갱신
        y = max(y, spot[j+1][1])
        # d[i-1] + i번째 건물만 포함한 통신범위로 d[i]값 계산
        # j+1번째 계산한 값과 비교 
        d[i] = min(d[i], d[j] + max(spot[i][0] - spot[j+1][0], y * 2))

print(d[N])