N, K = map(int,input().split())
quests = list(map(int,input().split()))

qq = sorted(quests)
# 버블이나 카운트 소트 사용하기에는 N의 최댓값이 300000이라...

EXP = 0
# 경험치 양 기록


for i in range(K):
    EXP += qq[i] * i
# 아케인스톤이 동시에 활성화되는 k까지는, 퀘스트를 깰 때마다
# 얻을 수 있는 경험치의 배수가 계속 증가함
# 즉 이때는 배수가 낮으므로, 낮은 경험치를 주는 퀘스트를 깨야 함

for i in range(K,N):
    EXP += qq[i] * K
# 최대 활성화 가능까지 아케인스톤을 모았다면, 이후 얻는 경험치의 양은
# k배수로 계속 더해주면 됨
# 최대 배수이므로, 높은 경험치의 퀘스트를 깨야 함

print(EXP)
# 얻을 수 있는 경험치의 최대치 출력