N = int(input())

l_list = []
for _ in range(N):
    start, end = map(int, input().split())
    l_list.append((start, end))

# 회의 끝 시간으로 정렬
# 끝나는 시간이 같다면 시작시간으로 두 번째 정렬
l_list = sorted(l_list, key=lambda l: (l[1],l[0]))


count = 1
# 가장 빨리 끝나는 회의 먼저 실행
end = l_list[0][1]

for i in range(1,N):
    # 앞 회의의 끝나는 시간보다 늦거나 같은 시간에 시작하는 회의 중
    # 끝나는 시간 시간이 빠른 회의 실행
    if l_list[i][0] >= end:
        count +=1
        end = l_list[i][1]

print(count)
