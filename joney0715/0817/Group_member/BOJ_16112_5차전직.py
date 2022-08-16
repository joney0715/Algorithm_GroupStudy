# 퀘스트 개수, 활성화된 스톤 수
n, k = map(int, input().split())

# 경험치
quest = list(map(int, input().split()))
# 스톤을 얻기위해 경험치가 낮은 것을 먼저 수행
quest = sorted(quest)

exp = 0
# 첫번째 퀘스트는 경험치를 못 얻으므로 두 번째부터
for i in range(1,n):
    # 활성화된 스톤 수 미달인 경우
    if i < k:
        exp += quest[i]*i
    
    # 전부 활성화된 경우
    # 퀘스트한 만큼 전부 스톤에 축적
    else:
        exp += quest[i]*k

print(exp)
