N = int(input())

cow_list = []
for _ in range(N):
    # 방문 시각, 검문 시간
    a, b = map(int, input().split())
    cow_list.append((a,b))

# 방문 시각으로 정렬, 검문 시간으로 2차 정렬
cow_list = sorted(cow_list, key=lambda x : (x[0], x[1]))

end = 0
# 방문한 소 한 마리씩 처리
for cow in cow_list:
    # 소가 방문한 시간이 전 소의 검문이 끝난 시간보다 늦다면
    if end <= cow[0]:
        # 도착 시간 + 검문 시간만큼 끝나는 시간 초기화
        end = cow[0] + cow[1]
    else:
        # 앞 소의 검문이 끝나기 전에 도착하면
        # 끝나는 동시에 검문이 시작하므로 기존 끝나는 시간에 검문시간 더하기
        end += cow[1]
print(end)

