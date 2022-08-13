N = int(input())
arrived = []
for n in range(N):
    start, time = map(int,input().split())
    arrived.append([start,time])
    # 소의 도착 시간, 검사 시간을 튜플로 리스트에 저장

for i in range(N-1,0,-1):
    for j in range(i):
        if arrived[j][0] > arrived[j+1][0]:
            arrived[j], arrived[j+1] = arrived[j+1], arrived[j]
# start 값을 기준으로 버블소트 진행

finish = 0
for i in arrived:
    if finish < i[0]:
        # 검사중인 소가 없는 경우

        finish = i[0]+i[1]
        # 검사 시작 시간 + 검사 지속 시간을 합한 값으로 갱신

    else: 
        # 검사중인 소가 있는 경우

        finish += i[1]
        # 검사가 끝나는 시간에 검사 지속 시간을 더해 줌

        
print(finish)