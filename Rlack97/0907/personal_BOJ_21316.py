# 스피카 풀이
# 2022-09-03

stars = [[] for _ in range(13)]
# 노드 리스트를 위한 빈 리스트 생성
# *13하면 값 다 복사되니까 주의

for i in range(1,13):
    x,y = map(int,input().split())
    stars[x].append(y)
    stars[y].append(x)
    # 서로 연결되어 있으므로 각자를 노드 리스트에 추가

# 스피카는 인접 노드가 3개이며, 그 노드들의 간선은 각각 3,2,1이다.
for s in range(1,13):
    # 그래프의 모든 노드들에 대해

    if len(stars[s]) == 3:
        # 인접 노드가 3개이며,

        spica = {1,2,3}
        cnt = set()

        for ss in stars[s]:
            cnt.add(len(stars[ss]))
            
        if cnt == spica:
            # 인접 노드들이 지닌 간선의 수가 1,2,3인 경우

            answer = s
            

print(answer)
