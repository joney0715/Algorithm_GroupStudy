# BOJ_15553_난로
# 220814

import sys

# 친구들 숫자
N, K = map(int, sys.stdin.readline().split())

T_list = [int(sys.stdin.readline()) for _ in range(N)]

max = 0
for t in T_list:
    if t >= max:
        max = t

time = [0] * t

for t in T_list:
    time[t-1] = 1

# 연속한 1의 덩어리 구하는 함수
def bulk_cnt(time):
    temp = time + [0]
    length = len(temp)
    cnt = 0
    for i in range(length-1):
        if temp[i] == 1 and temp[i+1] == 0:
            cnt += 1
    return cnt

cnt = bulk_cnt(time)
if cnt == K:
    print(time.count(1))
else:
    blank = 1
    status = False
    while status == False:
        # j는 범위의 첫번째 인덱스
        for j in range(max - blank - 1):
            if time[j] == 1 and time[j+1:j+blank+1] == [0] * blank and time[j+blank+1] == 1:
                for k in range(j+1, j+blank+1):
                    time[k] = 1
                cnt = bulk_cnt(time)
                if cnt == K:
                    status = True
                    break
        if status == False:
            blank += 1
    print(time.count(1))
