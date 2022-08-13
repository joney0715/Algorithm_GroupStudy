N,K = map(int,input().split())
guest = []

for n in range(N):
    t = int(input())
    guest.append(t)

blanktime = []
for n in range(N-1):
    blanktime.append(guest[n+1]-guest[n])

S = sorted(blanktime)
# 친구가 없는 시간의 길이를 리스트화 후 정렬

K -= 1
# 첫 친구의 방문 때 성냥을 하나 사용

firetime = 1
# 첫 친구의 방문에 켜 둔 불

for i in range(N-1):
    if K:
        firetime += 1
        S.pop()
        K-=1
    else:
        firetime += S.pop()
# 친구가 없는 시간이 가장 긴 구간을, 성냥을 하나 사용해서 1로 변환
# 성냥이 다 떨어지면 그냥 계속 켜둠

print(firetime)