N = int(input())
switch = [99] + (list(map(int,input().split())))
S = int(input())

def control(value):
    if value == 0:
        return 1
    elif value == 1:
        return 0
        # 스위치를 전환하는 함수

for s in range(S):
    sex, num = map(int,input().split())

    if sex == 1:
        for n in range(1,N+1):  # index 
            if n % num == 0:
                switch[n] = control(switch[n])
                # 남자일 경우, num으로 나누어지는 경우만 값을 변경
    else:
        switch[num] = control(switch[num])
        i = 1
        while num+i <= N and num-i >= 0:
            if switch[num+i] == switch[num-i]:
                switch[num+i] = control(switch[num+i])
                switch[num-i] = control(switch[num-i]) 
                i += 1
            else:
                break
            # 여자일 경우, 자기 앞뒤의 범위가 똑같으면 값을 변경


for r in range(1,N+1):
    print(switch[r], end = " ")
    if r%20 == 0:
        print()
        # 양식에 맞는 형태로 출력
