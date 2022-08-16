# BOJ_15553_난로
# 220814

import sys

# 친구들 숫자
N, k = map(int, sys.stdin.readline().split())

# 친구들 순서대로 받고 제일 큰 숫자와 동일한 길이의 리스트 생성
max_idx = 0
idx_list = []
for _ in range(N):
    idx = int(sys.stdin.readline())
    idx_list.append(idx)
    if idx >= max_idx:
        max_idx = idx

# max_idx 크기의 리스트 생성
arr = [0] * (max_idx + 1)

# 도착시간에 +1
for i in range(N):
    arr[ idx_list[i] ] += 1

# cnt 센다 > 비교 > 차이만큼 반복
# 가까운거 연결 > 거리 1있는지 체크 > 연결 > 거리 2 있는지 체크 > 연결 ...

# 연속한 1의 갯수 세는 cnt
# 전이 0이고 본인이 1인 순간만 cnt += 1
cnt = 0
for i in range(max_idx + 1):
    if arr[i - 1] == 0 and arr[i] == 1:
        cnt += 1
    else:
        pass

# cnt = k거나 cnt < k면 cnt가 출력값
# cnt > k면 cnt와 k의 차이만큼 연결을 반복
if cnt <= k:
    print(cnt)
else:
    # cnt가 k랑 같아질 때까지 반복
    # d는 1 사이의 인덱스 차이
    i, d = 0, 2
    while i + d <= max_idx:
        # i + d가 마지막 인덱스일때까지만
        if i + d <= max_idx:
            # 최소 거리 조건에 맞는 연결할 곳 찾으면
            if arr[i] == 1 and arr[i+d] == 1:
                for l in range(i + 1, i + d):
                    arr[l] = 1

                # 인덱스 차이 d인 1 사이 0으로 바꾸고 cnt 확인
                cnt = 0
                for j in range(max_idx + 1):
                    if arr[j - 1] == 0 and arr[j] == 1:
                        cnt += 1

                if cnt == k:
                    break
                else:
                    # 끝까지 다 확인했으면 거리 += 1
                    if i + d == max_idx:
                        d += 1
                        i = 0
                    else:
                        i += 1

            # 연결할 곳 못 찾으면
            else:
                if i + d == max_idx:
                    d += 1
                    i = 0
                else:
                    i += 1
        else:
            i = 0
            d += 1

    total = 0
    for i in range(max_idx+1):
        if arr[i] == 1:
            total += 1
    print(total)


