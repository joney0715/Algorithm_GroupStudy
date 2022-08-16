# BOJ_15553_난로
# 220814

import sys

# 친구들 숫자
N, K = map(int, sys.stdin.readline().split())

T_list = [int(sys.stdin.readline()) for _ in range(N)]
length = max(T_list)
time = [0] * length

for i in range(N):
    time[T_list[i] - 1] = 1

def bulk_cnt(time):
    temp = time + [0]
    length = len(temp)
    cnt = 0
    for i in range(length-1):
        if temp[i] == 1 and temp[i+1] == 0:
            cnt += 1
    return cnt

if bulk_cnt(time) == K:
    print(time.count(1))
else:
    blank = 1
    status = False
    while blank < length:
        for j in range(length - blank - 1):
            if time[j:j+blank+2] == [1] + [0] * blank + [1]:
                for k in range(j+1, j+blank+1):
                    time[k] = 1
                cnt = bulk_cnt(time)
                if bulk_cnt(time) == K:
                    status = True
                    break
        if status == False:
            blank += 1
        else:
            break
    print(time.count(1))
