
N,K = map(int,input().split())
guest = []
for n in range(N):
    t = int(input())
    tout = t+1
    guest.append((t,tout))
    # 튜플로 친구가 머문 구간을 리스트에 기록
print(guest)

if K == 1:
    firetime = guest[-1][1] - guest[0][0]

elif K == N:
    firetime = 0
    for k in guest:
        firetime += 1
else:
    newlist = []
    cnt = 0
    firetime = 0
    for i in range(N-1):
        if guest[i][1] == guest[i+1][0]:
            newlist.append((guest[i][0],guest[i+1][1]))
            # 붙어있는 구간대를 연결
        elif i !=0 and guest[i][0]  == guest[i-1][1]:
            continue
        else:
            newlist.append(guest[i])
        cnt+=1

    if guest[-2][1] != guest[-1][0]:
        newlist.append(guest[-1])
        cnt+=1

    while cnt > K:
        # 총 갯수가 K가 될 때까지
        for j in range(cnt-1):
            if newlist[j][1] + 1 == newlist[j+1][0]:
                newlist[j] = ((newlist[j][0],newlist[j+1][1]))
                newlist[j+1] = (0,0)
                cnt -= 1 
                # 두 구간 사이의 거리가 1이라면 구간을 합침
                
    for a in newlist:
        firetime += a[1] - a[0]


print(firetime)