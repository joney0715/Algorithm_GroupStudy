N = int(input())

N_list = list(map(int, input().split()))
# 입력 받은 숫자 정렬
N_list.sort()

target = int(input())

count = 0
# 양쪽 끝에서 중간으로 값을 좁혀오면서 검색
start = 0
end = N-1
# 시작과 끝이 엇갈리면 종료
while end > start:
    # 합이 타겟과 같으면 다음 계산을 위해 시작점 하나 늘리기
    if N_list[start] + N_list[end] == target:
        count += 1
        start += 1
    # 합이 타겟보다 크면 끝점을 이동시켜서 합을 작게 만듬
    elif N_list[start] + N_list[end] > target:
        end -= 1
    # 합이 타겟보다 작으면 시작점을 이동시켜서 합을 크게 만듬
    else:
        start += 1

print(count)